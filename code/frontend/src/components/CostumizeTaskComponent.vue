<script>
import axios from 'axios';
import { store } from './store';
export default {
    data() {
        return {
            allCases: []
        }
    },
    methods: {
        showValueOfSlider: function (value, label, description) {
            const labelForSlider = document.getElementById(label);
            let sliderValue = document.getElementById('amountTasks').value
            labelForSlider.innerHTML = `${sliderValue} ${description}`;
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
                <label for="amountTasks" class="form-label" id="labelAmount"> Aufgaben</label>
                <input type="range" min="1" max="15" step="1" name="amount" id="amountTasks" class="form-range"
                    @input="this.showValueOfSlider(this.value, 'labelAmount', 'Aufgaben')">
            </div>
            <div class="col-6">
                <label for="difficultyTasks" class="form-label" id="labelDifficulty"> Unterschiedliche
                    Sachverhalte</label>
                <input type="range" min="1" max="15" step="1" name="difficulty" id="difficultyTasks" class="form-range"
                    @input="this.showValueOfSlider(this.value, 'labelDifficulty', 'Unterschiedliche Sachverhalte')">
            </div>
        </div>
        <div class="row mb-3 justify-content-center">

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