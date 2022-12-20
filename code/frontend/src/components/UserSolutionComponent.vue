<script>
import axios from 'axios';
import { task_id } from './store';

export default {
    data() {
        return {
            options: [],
            rows: [
                {
                    'id': 0, 'select': "Sachverhalt auswählen", "law": '',
                    "num": '', "isCorrect": { "case_name": false, "law": false, "num": false }
                }
            ],
            allSolutions : []
        };
    },
    computed: {
        showMaxRows() {
            return Object.keys(this.options).length
        }
    },
    methods: {
        getOptions: function () {
            const url = "http://localhost:8000/select-options/" + task_id;
            axios.get(url).then((res) => {
                this.options = res.data;
            });
        },
        checkIfRowNecessary: function () {
            let maxRows = this.showMaxRows > 0 ? this.showMaxRows : null;
            return maxRows > this.rows.length ? true : false;
        },
        addRow: function () {
            const warningOrSuccessDiv = document.getElementById('warningOrSuccess');
            try {
                newId = this.rows[this.rows.length - 1]["id"] + 1
            } catch {
                newId = 0
            }
            if (this.checkIfRowNecessary()) {
                this.rows.push({
                    'id': newId, 'select': "Sachverhalt auswählen", "law": '',
                    "num": '', "isCorrect": { "case_name": false, "law": false, "num": false }
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
        checkCorrectInputs: function (row) {
            if (row.select in allSolutions) {
                // check if the Inputs match the correct solution inputs, set the elem of the row accordingly
                row.isCorrect.case_name = true;
                const correctSolution = allSolutions[row.select];

                row.law === correctSolution.law ? row.isCorrect.law = true : row.isCorrect.law = false;
                row.num === correctSolution.number ? row.isCorrect.num = true : row.isCorrect.num = false;

                console.log(row)
                this.evaluateCorrectnessOfRow(row.isCorrect, row);
            }
        },
        // set which task is solved by which row
        setCorrespondingRows: function (row) {
            for (let sol of correctSolutions) {
                row.select === sol.task ? sol.solved_by = row.id : null;
            }
        },
        solve: function () {
            const url = 'http://localhost:8000/solution/' + task_id
            axios.get(url).then((res) => {
                this.allSolutions = res.data
            });
            console.log(this.allSolutions);
            let areSolved = 0;
            // initialize dict to check if all tasks are correct
            for (const row of this.rows) {
                this.checkCorrectInputs(row);
                this.setCorrespondingRows(row)
                for (let sol of correctSolutions) {
                    // check if all rows are solved
                    if (row.id === sol.solved_by) {
                        row.isCorrect.case_name && row.isCorrect.law && row.isCorrect.num ? sol.solved = true : sol.solved = false;
                    }
                }
            }
            for (let solution of correctSolutions) {
                if (solution.solved) {
                    areSolved += 1;
                }
            }
            const successMsg = document.getElementById('warningOrSuccess');
            console.log(areSolved);
            if (areSolved === correctSolutions.length) {
                successMsg.innerHTML = "Alles gelöst";
                successMsg.className = "alert alert-success"
            }
            console.log(correctSolutions);
        },
        evaluateCorrectnessOfRow: function (isCorrect, row) {
            const caseInput = document.getElementById(row.id + "_case_name");
            const lawInput = document.getElementById(row.id + "_law");
            const sumInput = document.getElementById(row.id + "_num");

            if (isCorrect.case_name) {
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

            const delBtn = document.getElementById(row.id + '_del');
            isCorrect.case_name && isCorrect.law && isCorrect.num ? delBtn.disabled = true : delBtn.disabled = false;
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
                                    <option :value="opt.name" v-for="opt in options">{% raw %} {{ opt.name }} {% endraw
                                        %}
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
                                    @click="deleteRow(row)">Löschen</button>
                            </div>
                        </div>
                        <div class="row mb-3">
                            <input type="number" class="form-control" id="zvE">
                        </div>
                    </div>
                </div>
                <div class="d-flex flex-row m-3">
                    <div class="col">
                        <button type="button" name="submitSolution" class="btn btn-primary" @click="solve">Aufgabe
                            lösen</button>
                    </div>
                    <div class="col" id="warningOrSuccess">

                    </div>
                    <div class="col">
                        <button id="addRow" type="button" class="btn btn-success" @click="addRow">Reihe
                            hinzufügen</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>