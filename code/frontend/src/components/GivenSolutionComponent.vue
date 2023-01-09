<script>
import axios from 'axios';
import { store } from './store';

export default {
    data() {
        return {
            solutions: [],
            zve: null
        }
    },
    methods: {
        getSolution() {
            if (store.task_id !== null) {
                const url = "http://localhost:8000/";
                axios.get(url + "solution/" + store.task_id).then((res) => {
                    this.solutions = res.data;
                    console.log(this.solutions)
                }).catch((error) => {
                    store.error = error
                });
    
                axios.get(url + "zve/" + store.task_id).then((res) => {
                    this.zve = res.data;
                }).catch((error) => {
                    store.error = error
                })
            }
        }
    }
}
</script>
<template>
    <div class="container-fluid">
        <div class="col">
            <a @click="getSolution()" class="btn btn-primary" data-bs-toggle="collapse" href="#solution" role="button"
                aria-expanded="false" aria-controls="solution">
                Lösung anzeigen
            </a>
        </div>
        <div class="col">
            <div class="collapse" id="solution">
                <div class="card card-body bg-dark mb-3">
                    <table class="table table-dark table-striped">
                        <thead>
                            <tr>
                                <td>Sachverhalt</td>
                                <td>Gesetzesgrundlage</td>
                                <td>Summe des Sachverhalts</td>
                            </tr>
                        </thead>
                        <template v-if="solutions !== []">
                            <template v-for="solution in this.solutions">
                                <tr>
                                    <td>
                                        {{ solution.case_name }}
                                    </td>
                                    <td>
                                        {{ solution.law }}
                                    </td>
                                    <td>
                                        {{ solution.number }}
                                    </td>
                                </tr>
                            </template>
                        </template>
                        <tr>
                            <td>zvE</td>
                            <td></td>
                            <td>{{ zve }}</td>
                        </tr>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>