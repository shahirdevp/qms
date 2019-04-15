import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Dashboard/Dashboard.vue';
import Login from './views/Auth/Login.vue';
import subcategory from './views/Dashboard/SubCategory.vue';


//  hr
import Hrlist from './views/Hr/Hr.vue';
import Hrdetail from './views/Hr/Hrdetail.vue';
import EmployeeList from './views/Hr/EmployeeList.vue';
import EmployeeDetail from './views/Hr/EmployeeDetail.vue';
import compentency from './views/Hr/Compentency.vue';
import compentencyDetail from './views/Hr/CompentencyDetail.vue';
import TrrList from './views/Hr/TrainingReqList.vue';
import TrrDetails from './views/Hr/TrainingReqDetail.vue';
import anualtraing from './views/Hr/AnualTraining.vue';
import anualtraingDetails from './views/Hr/AnualTrainingDetail.vue';
import trEvalution from './views/Hr/TrainingEvalution.vue';
import skillmatrix from './views/Hr/SkillMatrix.vue';
import skillmatrixDetail from './views/Hr/SkillMatrixDetail.vue';
import skillmatrixInsert from './views/Hr/SkillMatrixInsert.vue';
import settingdepartment from './views/Setting/Setting.vue';
import marketingenquiry from './views/Marketing/MarketingEnquiry.vue';
import marketingenquiryinsert from './views/Marketing/MarketingEnquiryInsert.vue';
import feasibilitydetail from './views/Marketing/FeasibilityDetail.vue';
import feasibilityinsert from './views/Marketing/FeasibilityInsert.vue';



Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'login',
      component: Login,
    },
    {
      path: '/dashboard',
      name: 'home',
      component: Home,
    },
    {
      path: '/hr-list',
      name: 'hrlist',
      component: Hrlist,
    },

    {
      path: '/hr-detail/:id',
      name: 'Hrdetail',
      component: Hrdetail,
    },
    {
      path: '/hr',
      name: 'subcategory',
      component: subcategory,
    },
    {
      path: '/employee',
      name: 'EmployeeList',
      component: EmployeeList,
    },
    {
      path: '/employee/:id',
      name: 'EmployeeDetail',
      component: EmployeeDetail,
    },
    {
      path: '/compentency-matrix',
      name: 'compentency',
      component: compentency,
    },
    {
      path: '/compentency-matrix/:id',
      name: 'compentencyDetail',
      component: compentencyDetail,
    },
    {
      path: '/trining-request-register',
      name: 'TrainingRequestRegisterList',
      component: TrrList,
    },
    {
      path: '/trining-request-register/:id',
      name: 'TrainingRequestRegisterDetail',
      component: TrrDetails,
    },
    {
      path: '/anual-training-plan',
      name: 'Anual training',
      component: anualtraing,
    },
    {
      path: '/anual-training-plan/:id',
      name: 'Anual training details',
      component: anualtraingDetails,
    },
    {
      path: '/training-evalution-record',
      name: 'Training evalution record',
      component: trEvalution,
    },
    {
      path: '/skill-matrix',
      name: 'Skill matrix list',
      component: skillmatrix,
    },
    {
      path: '/skill-matrix/:id',
      name: 'Skill matrix',
      component: skillmatrixDetail,
    },
    {
      path: '/skill-matrix-insert',
      name: 'Skill matrix insert',
      component: skillmatrixInsert,
    },
    {
      path: '/department',
      name: 'Department',
      component: settingdepartment,
    },
    {
      path: '/marketing-enquiry',
      name: 'Marketing Enquiry',
      component: marketingenquiry,
    },
    {
      path: '/marketing-enquiry-insert',
      name: 'Marketing Enquiry Insert',
      component: marketingenquiryinsert,
    },
    
    {
      path: '/feasibility',
      name: 'Feasibility',
      component: feasibilitydetail,
    },
    {
      path: '/feasibility-insert',
      name: 'Feasibility Insert',
      component: feasibilityinsert,
    },
  ],
});

