<script>
import axios from 'axios';
import { store } from './store';
export default {
    data() {
        return {
            allCases: [],
            difficultyValue: 3,
            amountValue: 8,
            needed: []
        }
    },
    computed: {
        amountSlider() {
            return this.amountValue;
        },
        difficultySlider() {
            return this.difficultyValue;
        },
        taskId() {
             return store.task_id;
        }
    },
    methods: {
        getCasesToChoose: function () {
            const url = "http://localhost:8000/cases-to-choose";
            axios.get(url).then((res) => {
                this.allCases = res.data;
            });

        },
        isVariableAndNotEmpty(variable) {
            if (Array.isArray(variable) && variable.length > 0) {
                return true;
            } else if (Number.isInteger(variable) || typeof variable === "string") {
                return true;
            }
        },
        buildURL() {
            const params = {
                difficulty: this.difficultyValue,
                amount: this.amountValue,
                needed: this.needed
            }
            const queryString = Object.keys(params).map(key => (this.isVariableAndNotEmpty(params[key]) ? `${key}=${params[key]}` : null)).filter(Boolean).join('&');
            const url = `http://localhost:8000/get-task?${queryString}`;
            return url;
        },
        async getTask() {
            const url = this.buildURL();
            console.log(url)
            await axios.get(url)
                .then((res) => {
                    store.sentences = res.data.sentences;
                    store.task_id = res.data.id;
                })
                .catch((error) => {
                    console.log(error);
                });
        }
    },
    mounted() {
        this.getCasesToChoose();
    }
}
</script>
<template>
    <form action="" method="">
        <div class="row mb-3 justify-content-center">
            <div class="col-6">
                <label for="amountTasks" class="form-label" id="labelAmount">{{ amountSlider }} Sachverhalte</label>
                <input type="range" v-model="amountValue" min="1" max="15" step="1" id="amountTasks" class="form-range">
            </div>
            <div class="col-6">
                <label for="difficultyTasks" class="form-label" id="labelDifficulty">{{ difficultySlider }}
                    Unterschiedliche Sachverhalte</label>
                <input type="range" v-model="difficultyValue" min="1" max="15" step="1" id="difficultyTasks"
                    class="form-range">
            </div>
        </div>
        <div class="row mb-3 justify-content-center">

            <div class="col-auto">
                <button class="btn btn-secondary" type="button" data-bs-toggle="collapse" data-bs-target="#neededSelect"
                    aria-expanded="false" aria-controls="neededSelect">
                    Muss enthalten sein
                </button>
            </div>
            <div class="col-auto">
                <button @click="this.getTask()" type="button" value="generate" id="generateBtn"
                    class="btn btn-primary float-right">Generieren</button>
            </div>
        </div>
        <div class="row mb-3">
            <div class="collapse" id="neededSelect">
                <div class="row">
                    <div class="row row-cols-3">
                        <div class="col" v-for="key in allCases">
                            <div class="form-check form-check-inline">
                                <input v-model="needed" class="form-check-input" name="needed" type="checkbox"
                                    :value=key :id=key>
                                <label class="form-check-label" :for=key>
                                    {{ key }}
                                </label>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </form>
</template>