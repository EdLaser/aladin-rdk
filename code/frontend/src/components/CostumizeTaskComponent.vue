<script>
import axios from 'axios';
import { store } from './store';
export default {
    data() {
        return {
            allCases: [],
            value: 8
        }
    },
    methods: {
        showValueOfSlider: function (value) {
            const labelForSlider = document.getElementById('labelForSlider');
            this.value = document.getElementById('amountTasks').value
            labelForSlider.innerHTML = `${value} Aufgaben`;
        }, getCasesToChoose: function () {
            const url = "http://localhost:8000/cases-to-choose";
            axios.get(url).then((res) => {
                this.allCases = res.data;
            });
        },
        getTask() {
            const url = 'http://localhost:8000/get-task';
            axios.get(url)
                .then((res) => {
                    store.sentences = res.data.sentences;
                    store.task_id = res.data.id;
                })
                .catch((error) => {
                    console.log(error);
                });
        }
    },
}
</script>
<template>
    <form action="" method="post">
        <div class="row mb-3 justify-content-center">
            <div class="col-6">
                <label for="amountTasks" class="form-label" id="labelForSlider"> Aufgaben</label>
                <input type="range" min="1" max="15" step="1" name="amount" id="amountTasks" class="form-range"
                    @input="showValueOfSlider(this.value)">
            </div>
        </div>
        <div class="row mb-3 justify-content-center">
            <div class="col-auto">
                <select class="form-select" aria-label="Schwierigkeit auswählen" name="difficulty" id="selectDif">
                    <option selected value="0">Zufällig</option>
                    <option value="1">Leicht</option>
                    <option value="2">Mittel</option>
                    <option value="3">Schwer</option>
                </select>
                <label for="selectDif" class="form-label">Schwierigkeit</label>
            </div>
            <div class="col-auto">
                <button class="btn btn-secondary" type="button" data-bs-toggle="collapse" data-bs-target="#neededSelect"
                    aria-expanded="false" aria-controls="neededSelect">
                    Muss enthalten sein
                </button>
            </div>
        </div>
        <div class="row mb-3">
            <div class="collapse" id="neededSelect">
                <div class="row">
                    <div class="row row-cols-3">
                        <div class="col" v-for="key in allCases">
                            <div class="form-check form-check-inline">
                                <input class="form-check-input" name="needed" type="checkbox" :value=key :id=key>
                                <label class="form-check-label" :for=key>
                                    {{ key }}
                                </label>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="row mb-3 justify-content-center">
            <div class="col-auto">
                <button @click="this.getTask()" type="button" value="generate" id="generateBtn"
                    class="btn btn-primary float-right">Generieren</button>
            </div>
        </div>
    </form>
</template>