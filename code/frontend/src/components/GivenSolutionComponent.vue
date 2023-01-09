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
            id = store.task_id;
            axios.get("localhost:8000/" + id).then((res) => {
                this.solutions = res.data;
            }).catch((error) => {
                store.error = error
            });
            
            axios.get("localhost:8000/zve/" + id).then((res) => {
                this.zve = res.data;
            }).catch((error) => {
                store.error = error
            })
        }
    }
}
</script>
<template>
    <div class="col">
        <a @click="" class="btn btn-primary" data-bs-toggle="collapse" href="#solution" role="button"
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
                    <tr>
                        <td>
                            {{ value.case_name }}
                        </td>
                        <td>
                            {{ value.law }}
                        </td>
                        <td>
                            {{ value.number }}
                        </td>
                    </tr>
                    <tr>
                        <td>zvE</td>
                        <td></td>
                        <td>{{ sum }}</td>
                    </tr>
                </table>
            </div>
        </div>
    </div>
</template>