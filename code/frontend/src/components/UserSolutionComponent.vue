<script>
import axios from 'axios';
import { store } from './store';

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
            zve: 0
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
        }
    },
    methods: {
        reset() {
            this.options = [""],
                this.rows = [
                    {
                        'id': 0, 'select': "Sachverhalt auswählen", "law": '',
                        "num": null
                    }
                ]
            this.correct = {}
            this.allSolved = false
            this.zve = 0
        },
        getOptions: function () {
            const url = "http://localhost:8000/select-options/" + store.task_id;
            axios.get(url).then((res) => {
                this.options = res.data;
            }).catch((error) => {
                store.error = error
            });
        },
        solveTask() {
            const url = 'http://localhost:8000/solve/' + store.task_id
            const data = JSON.stringify(this.rows);
            axios.post(url, data, { headers: { 'Content-Type': 'application/json' } }).then((res) => {
                this.correct = res.data.given
                this.allSolved = res.data.all_solved
                console.log(res.data)
            }).catch((error) => {
                store.error = error.response.data.detail;
            });

            // only is set if default values are not set ?!
            for (const [key, value] of Object.entries(this.correct)) {
                console.log(`${key}: ${value}`);
                this.evaluateCorrectnessOfRow(key, value)
            }

            const successMsg = document.getElementById('warningOrSuccess');

            if (this.allSolved === true) {
                successMsg.innerHTML = "Alles gelöst";
                successMsg.className = "alert alert-success"
            }
        },
        checkIfRowNecessary: function () {
            let maxRows = this.showMaxRows > 0 ? this.showMaxRows : null;
            return maxRows > this.rows.length ? true : false;
        },
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
                        <input type="number" class="form-control" id="zvE" placeholder="zvE">
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