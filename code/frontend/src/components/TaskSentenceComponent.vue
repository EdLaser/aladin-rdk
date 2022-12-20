<script>
import axios from 'axios';

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