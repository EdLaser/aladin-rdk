<script>
import axios from 'axios';
import { store } from './store';
import { toHandlers } from 'vue';

export default {
    data() {
        return {
            options: [""],
            rows: [
                {
                    'id': 0, 'select': "Sachverhalt auswählen", "law": '',
                    "num": null
                }
            ],
            correct: {},
            allSolved: false,
            zve: false,
            zveValue: null
        };
    },
    computed: {
        showMaxRows() {
            return Object.keys(this.options).length
        },
        task_id() {
            return store.task_id;
        }
    },
    watch: {
        task_id() {
            console.log(this.task_id);
            this.reset();
            this.getOptions();

            const successMsg = document.getElementById('warningOrSuccess');
            successMsg.innerHTML = "";
            successMsg.className = "";

            if (!store.is_new) {
                let i = 0;
                let rows = [];
                for (const type in store.done_solutions) {
                    if (store.done_solutions[type]) {
                        rows.push({ 'id': i, 'select': type, 'law': store.done_solutions[type].law ||= '', 'num': store.done_solutions[type].num ||= null })
                    }
                    this.correct[i] = { 'name': store.done_solutions[type].name, 'law': store.done_solutions[type].law, 'num': store.done_solutions[type].num }
                    i++;
                }
                rows.length > 0 ? this.rows = rows : this.rows = [{ 'id': 0, 'select': "Sachverhalt auswählen", "law": '', "num": null }];
            }
        },
        /**
         * Iterates through the `correct` data property of the component and evaluates
         * the correctness of each row using the `evaluateCorrectnessOfRow()` function.
         * If all rows are correct, updates the `allSolved` data property to `true`.
         * Also checks the `zve` data property of the component and, if it is present and
         * all rows are correct, updates the UI to display a success message.
         * @function
         * @name correct
         * @returns {void} This function does not return anything, but updates the component's
         * `allSolved` and UI `successMsg` data properties if all rows are correct and `zve` is present.
         */
        correct() {
            for (const [key, value] of Object.entries(this.correct)) {
                this.evaluateCorrectnessOfRow(key, value)
            }

            const successMsg = document.getElementById('warningOrSuccess');
            this.checkZve()

            if (this.allSolved === true && this.zve) {
                successMsg.innerHTML = "Alles gelöst";
                successMsg.className = "alert alert-success"
            }
        }
    },
    methods: {
        /**
         * Resets the component's data properties and UI elements to their initial state.
         * @function
         * @name reset
         * @returns {void} This function does not return anything, but updates the component's
         * data properties and UI elements to their initial state.
         */
        reset() {
            this.options = [""],
                this.rows = [
                    {
                        'id': 0, 'select': "Sachverhalt auswählen", "law": '',
                        "num": null
                    }
                ]
            for (let row of this.rows) {
                document.getElementById(row.id + "_case_name").className = "form-control"
                document.getElementById(row.id + "_law").className = "form-control"
                document.getElementById(row.id + "_num").className = "form-control"
                document.getElementById("zvE").className = "form-control"
            }
            this.correct = {}
            this.allSolved = false
            this.zve = false
            this.zveValue = null
        },
        /**
         * Checks whether the user-entered ZVE value matches the correct ZVE for the current task,
         * and updates the component's `zve` property accordingly.
         * @function
         * @name checkZve
         * @returns {void} This function does not return anything, but updates the component's `zve`
         * property based on the comparison of the user-entered ZVE value and the correct ZVE for the
         * current task.
         */
        checkZve() {
            axios.get("http://localhost:8000/zve/" + this.task_id)
                .then((res) => {
                    this.zve = this.zveValue === res.data ? true : false;
                }).catch((error) => {
                    store.error = error
                });
        },
        /**
         * Retrieves the options (i.e., possible values) for the "law" dropdown menu in each row of the table
         * based on the current task ID, and updates the component's `options` property accordingly.
         * @function
         * @name getOptions
         * @returns {void} This function does not return anything, but updates the component's `options`
         * property based on the options retrieved from the server.
         */
        getOptions: function () {
            const url = "http://localhost:8000/select-options/" + store.task_id;
            axios.get(url).then((res) => {
                this.options = res.data;
            }).catch((error) => {
                store.error = error
            });
        },
        /**
         * Sends a POST request to solve a task with a given ID.
         * 
         * @function solveTask
         * @throws Will throw an error if the request fails.
         * @returns {Promise<void>} A promise that resolves if the request is successful.
         */
        solveTask() {
            const url = 'http://localhost:8000/solve/' + store.task_id
            const data = JSON.stringify(this.rows);
            axios.post(url, data, { headers: { 'Content-Type': 'application/json' } }).then((res) => {
                this.correct = res.data.given
                this.allSolved = res.data.all_solved
            }).catch((error) => {
                store.error = error.response.data.detail;
            });
        },
        checkIfRowNecessary: function () {
            let maxRows = this.showMaxRows > 0 ? this.showMaxRows : null;
            return maxRows > this.rows.length ? true : false;
        },
        /**
         * Adds a new row to a table if necessary, or displays a warning message if the maximum number of rows has already been reached.
         *
         * @param None
         * @returns None
         */
        addRow: function () {
            let newId = 0;
            const warningOrSuccessDiv = document.getElementById('warningOrSuccess');
            try {
                newId = this.rows[this.rows.length - 1]["id"] + 1
            } catch {
                newId = 0
            }
            if (this.checkIfRowNecessary()) {
                this.rows.push({
                    'id': newId, 'select': "Sachverhalt auswählen", "law": '',
                    "num": null
                });
            } else {
                warningOrSuccessDiv.className = "alert alert-danger";
                warningOrSuccessDiv.innerHTML = "Mehr Reihen brauchst du nicht."

                setTimeout(function () {
                    warningOrSuccessDiv.innerHTML = '';
                    warningOrSuccessDiv.className = '';
                }, 4000);
                document.getElementById('addRow').disabled = true
            }
        },
        /**
         * Deletes a row from a table and updates the table if necessary.
         *
         * @param {Object} row - The row to be deleted.
         * @return None
         */
        deleteRow: function (row) {
            const filteredRow = this.rows.filter(element => element !== row);
            this.rows = filteredRow;
            if (this.checkIfRowNecessary()) {
                document.getElementById('addRow').disabled = false
                document.getElementById('warningOrSuccess').innerHTML = ""
                document.getElementById('warningOrSuccess').className = ""
            } else {
                document.getElementById('addRow').disabled = true
            }
        },
        /**
         * Evaluates the correctness of a row in a table and updates the row's appearance and functionality accordingly.
         *
         * @param {string} id - The ID of the row to be evaluated.
         * @param {Object} isCorrect - An object containing Boolean values that indicate whether the case, law, and sum inputs in the row are correct.
         * @return None
         */
        evaluateCorrectnessOfRow: function (id, isCorrect) {
            const caseInput = document.getElementById(id + "_case_name");
            const lawInput = document.getElementById(id + "_law");
            const sumInput = document.getElementById(id + "_num");
            if (isCorrect.name) {
                caseInput.className = "form-control border-success border border-5";
                caseInput.disabled = true;
            } else {
                caseInput.className = "form-control border-danger border border-5";
            }

            if (isCorrect.law) {
                lawInput.className = "form-control border-success border border-5";
                lawInput.disabled = true;
            } else {
                lawInput.className = "form-control border-danger border border-5";
            }

            if (isCorrect.num) {
                sumInput.className = "form-control border-success border border-5";
                sumInput.disabled = true;
            } else {
                sumInput.className = "form-control border-danger border border-5";
            }

            const zveElem = document.getElementById('zvE');
            if (this.zve) {
                zveElem.className = "form-control border-success border border-5";
                zveElem.disabled = true;
            } else {
                zveElem.className = "form-control border-danger border border-5"
            }


            const delBtn = document.getElementById(id + '_del');
            isCorrect.name && isCorrect.law && isCorrect.num ? delBtn.disabled = true : delBtn.disabled = false;
        }
    }
}
</script>
<template>
    <div class="container-fluid" id="multiRowForm">
        <!-- Gesamte Column -->
        <div class="col-xs-12">
            <!-- Reihe für einen Lösungsansatz -->
            <form action="" method="">
                <div class="row form-row" v-for="row in rows">
                    <!-- Innere Column im Lösungsansatz -->
                    <div class="col col-xs-12">
                        <div class="row mb-3">
                            <div class="col">
                                <select :name="row.id + '_case_name'" :id="row.id + '_case_name'" class="form-control"
                                    v-model="row.select">
                                    <option selected disabled>Sachverhalt auswählen</option>
                                    <option :value="opt.name" v-for="opt in options">{{ opt.name }}
                                    </option>
                                </select>
                            </div>
                            <div class="col">
                                <input type="text" class="form-control" :id="row.id + '_law'"
                                    placeholder="Gesetzesgrundlage" v-model="row.law" :name="row.id + '_law'">
                            </div>
                            <div class="col">
                                <input type="number" class="form-control" :id="row.id + '_num'" placeholder="Summe"
                                    v-model="row.num" :name="row.id + '_num'">
                            </div>
                            <div class="col">
                                <button class="btn btn-danger" :id="row.id + '_del'"
                                    @click="this.deleteRow(row)">Löschen</button>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="d-flex flex-row mb-3">
                    <div class="col-xs-2">
                        <label for="zvE">zu versteuerndes Einkommen</label>
                        <input type="number" v-model="zveValue" class="form-control" id="zvE" placeholder="zvE">
                    </div>
                </div>
                <div class="d-flex flex-row m-3">
                    <div class="col">
                        <button type="button" name="submitSolution" class="btn btn-primary"
                            @click="this.solveTask()">Aufgabe
                            lösen</button>
                    </div>
                    <div class="col" id="warningOrSuccess">

                    </div>
                    <div class="col">
                        <button id="addRow" type="button" class="btn btn-success" @click="this.addRow()">Reihe
                            hinzufügen</button>
                    </div>
                </div>
            </form>
            <div id="debug">

            </div>
        </div>
    </div>
</template>