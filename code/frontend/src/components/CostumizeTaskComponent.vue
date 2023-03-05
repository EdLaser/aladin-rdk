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
        /**
         * Fetches a list of cases to choose from the server and updates the component's
         * allCases data property with the result.
         * @function
         * @name fetchCasesToChoose
         * @returns {void}
         * @throws {Error} If an error occurs during the API request, the error message is not handled.
         */
        getCasesToChoose: function () {
            const url = "http://localhost:8000/cases-to-choose";
            axios.get(url).then((res) => {
                this.allCases = res.data;
            });

        },
        /**
         * Checks if a given variable is not empty and of a valid type (array, integer, or string).
         * @function
         * @name isVariableAndNotEmpty
         * @param {*} variable - The variable to be checked.
         * @returns {boolean} True if the variable is not empty and of a valid type, false otherwise.
         */
        isVariableAndNotEmpty(variable) {
            if (Array.isArray(variable) && variable.length > 0) {
                return true;
            } else if (Number.isInteger(variable) || typeof variable === "string") {
                return true;
            }
        },
        /**
         * Builds a URL string with the specified query parameters based on the component's
         * difficultyValue, amountValue, and needed data properties.
         * @function
         * @name buildURL
         * @returns {string} A URL string with the specified query parameters.
         */
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
        /**
         * Fetches a task from the server using the API endpoint constructed from the
         * component's difficultyValue, amountValue, and needed data properties, and
         * updates the component's sentences and task_id data properties with the result.
         * @function
         * @name getTask
         * @returns {Promise<void>} A Promise that resolves when the task has been fetched and the
         * component's data properties have been updated.
         * @throws {Error} If an error occurs during the API request, the error message is logged to the console.
         */
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
            store.is_new = true;
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