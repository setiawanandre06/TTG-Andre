<template>
    <div class="list row">
        <div class="col-md-6">
            <h4>Employees List</h4>
            <ul class="list-group">
                <li class="list-group-item"
                    :class="{ active: index == currentIndex }"
                    v-for="(employee, index) in employees"
                    :key="index"
                    @click="setActiveEmployee(employee, index)"
                >
                    {{ employee.name }}
                </li>
            </ul>
  
            <button class="m-3 btn btn-sm btn-danger" @click="removeAllEmployees">
                Remove All
            </button>
        </div>
        <div class="col-md-6">
            <div v-if="currentEmployee">
                <h4>Employee</h4>
                <div>
                    <label><strong>Name:</strong></label> {{ currentEmployee.name }}
                </div>
                <div>
                    <label><strong>Email:</strong></label> {{ currentEmployee.email }}
                </div>
        
                <router-link :to="'/employees/' + currentEmployee.id" class="badge badge-warning">Edit</router-link>
                </div>
                <div v-else>
                <br />
                <p>Please click on a Employee...</p>
            </div>
        </div>
    </div>
</template>
  
<script>
    import EmployeeDataService from "../services/EmployeeDataService";

    export default {
        name: "employees-list",
        data() {
            return {
                employees: [],
                currentEmployee: null,
                currentIndex: -1,
                name: ""
            };
        },
        methods: {
            retrieveEmployees() {
            EmployeeDataService.getAll()
                .then(response => {
                    this.employees = response.data;
                    console.log(response.data);
                })
                .catch(e => {
                    console.log(e);
                });
            },

            refreshList() {
                this.retrieveEmployees();
                this.currentEmployee = null;
                this.currentIndex = -1;
            },

            setActiveEmployee(employee, index) {
                this.currentEmployee = employee;
                this.currentIndex = employee ? index : -1;
            },

            removeAllEmployees() {
                EmployeeDataService.deleteAll()
                .then(response => {
                    console.log(response.data);
                    this.refreshList();
                })
                .catch(e => {
                    console.log(e);
                });
            },
        },
        mounted() {
            this.retrieveEmployees();
        }
    };
</script>

<style>
    .list {
        text-align: left;
        max-width: 750px;
        margin: auto;
    }
</style>