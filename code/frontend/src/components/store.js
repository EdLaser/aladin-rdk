import { reactive } from 'vue';

export let store = reactive({
    task_id: null,
    sentences: [],
    error: "",
    is_new: true,
    done_solutions: {}
});