<script>
import axios from 'axios';
import { task_id } from './store';

export default {
    data() {
        return {
            task_id: null,
            sentences: []
        };
    },
    methods: {
        getTask() {
            const url = 'http://localhost:8000/get-task';
            axios.get(url)
                .then((res) => {
                    this.sentences = res.data.sentences;
                    task_id = res.data.id;
                })
                .catch((error) => {
                    console.log(error);
                });
        }
    },
    created() {
        this.getTask();
    }
}
</script>
<template>
    <div class="container">
        <p>
            <template v-for="sentence in sentences">
                {{ sentence }}
            </template>
        </p>
    </div>
</template>