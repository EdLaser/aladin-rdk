<script>
import CostumizeTaskComponent from './CostumizeTaskComponent.vue';
import TaskSentenceComponent from './TaskSentenceComponent.vue';
import UserSolutionComponent from './UserSolutionComponent.vue';
import ErrorComponent from './ErrorComponent.vue';
import GivenSolutionComponent from './GivenSolutionComponent.vue';
import AllTasksComponent from './AllTasksComponent.vue';

export default {
    components: {
        TaskSentenceComponent,
        UserSolutionComponent,
        CostumizeTaskComponent,
        ErrorComponent,
        GivenSolutionComponent,
        AllTasksComponent
    }
}
</script>
<template>
    <h1>Generierung einer Aufgabe</h1>
    <p class="lead">
        Hier werden Aufgaben zum Steuerrecht generiert!
    </p>
    <div class="container w-100 mb-5">
        <div class="row justify-content-center">
            <div class="col">
                <AllTasksComponent />
            </div>
        </div>
        <div class="row justify-content-center">
            <div class="col">
                <TaskSentenceComponent />
            </div>
            <div class="col">
                <CostumizeTaskComponent />
            </div>
        </div>
    </div>
    <div class="container">
        <div class="d-flex flex-row bd-highlight mb-3">
            <UserSolutionComponent />
        </div>
        <div class="d-flex flex-row bd-highlight mb-3">
            <GivenSolutionComponent />
        </div>
    </div>
    <div class="container">
        <div class="d-flex flex-row bd-highlight mb-3">
            <ErrorComponent />
        </div>
    </div>
</template>