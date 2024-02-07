import { createWebHistory, createRouter } from "vue-router";

const routes =  [
    {
        path: "/",
        alias: "/employees",
        name: "employees",
        component: () => import("./components/EmployeesList")
    },
    {
        path: "/employees/:id",
        name: "employee-details",
        component: () => import("./components/Employee")
    },
    {
        path: "/add",
        name: "add",
        component: () => import("./components/AddEmployee")
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;