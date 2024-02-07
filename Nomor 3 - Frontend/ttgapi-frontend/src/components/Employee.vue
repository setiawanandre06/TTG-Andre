<template>
    <div v-if="currentEmployee" class="edit-form">
        <h4>Employee</h4>
        <form>
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" class="form-control" id="title"
                    v-model="currentEmployee.name"
                />
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="text" class="form-control" id="description"
                    v-model="currentEmployee.email"
                />
            </div>
        </form>

        <button class="badge badge-danger mr-2" @click="deleteEmployee">
            Delete
        </button>

        <button type="submit" class="badge badge-success" @click="updateEmployee">
            Update
        </button>

        <p>{{ message }}</p>
    </div>

    <div v-else>
    <br />
    <p>Please click on a Employee...</p>
    </div>
</template>

<script>
import EmployeeDataService from "../services/EmployeeDataService";

export default {
    name: "employee",
    data() {
    return {
        currentEmployee: null,
        message: ''
    };
    },
    methods: {
    getEmployee(id) {
        EmployeeDataService.get(id)
        .then(response => {
            this.currentEmployee = response.data;
            console.log(response.data);
        })
        .catch(e => {
            console.log(e);
        });
    },

    updateEmployee() {
        EmployeeDataService.update(this.currentEmployee.id, this.currentEmployee)
        .then(response => {
            console.log(response.data);
            this.message = 'The employee was updated successfully!';
        })
        .catch(e => {
            console.log(e);
        });
    },

    deleteEmployee() {
        EmployeeDataService.delete(this.currentEmployee.id)
        .then(response => {
            console.log(response.data);
            this.$router.push({ name: "employees" });
        })
        .catch(e => {
            console.log(e);
        });
    }
    },
    mounted() {
        this.message = '';
        this.getEmployee(this.$route.params.id);
    }
};
</script>

<style>
.edit-form {
    max-width: 300px;
    margin: auto;
}
</style>