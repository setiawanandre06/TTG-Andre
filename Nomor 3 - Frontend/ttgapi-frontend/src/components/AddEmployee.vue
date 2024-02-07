<template>
    <div class="submit-form">
        <div v-if="!submitted">
            <div class="form-group">
                <label for="name">Name</label>
                <input
                    type="text"
                    class="form-control"
                    id="name"
                    required
                    v-model="employee.name"
                    name="name"
                />
            </div>
    
            <div class="form-group">
                <label for="email">Email</label>
                <input
                    class="form-control"
                    id="email"
                    required
                    v-model="employee.email"
                    name="email"
                />
            </div>
    
            <button @click="saveEmployee" class="btn btn-success">Submit</button>
        </div>
    
        <div v-else>
            <h4>You submitted successfully!</h4>
            <button class="btn btn-success" @click="newEmployee">Add</button>
        </div>
    </div>
</template>

<script>
import EmployeeDataService from "../services/EmployeeDataService";

export default {
    name: "add-employee",
    data() {
        return {
            employee: {
                id: null,
                name: "",
                email: "",
                published: false
            },
            submitted: false
        };
    },
    methods: {
        saveEmployee() {
            var data = {
                name: this.employee.name,
                email: this.employee.email
            };

            EmployeeDataService.create(data)
                .then(response => {
                    this.employee.id = response.data.id;
                    console.log(response.data);
                    this.submitted = true;
            })
            .catch(e => {
                console.log(e);
            });
        },
        
        newEmployee() {
            this.submitted = false;
            this.employee = {};
        }
    }
};
</script>

<style>
.submit-form {
    max-width: 300px;
    margin: auto;
}
</style>