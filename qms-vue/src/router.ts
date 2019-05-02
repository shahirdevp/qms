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

import skillmatrix from './views/Hr/SkillMatrix/SkillMatrix.vue';
import skillmatrixDetail from './views/Hr/SkillMatrix/SkillMatrixDetail.vue';
import skillmatrixInsert from './views/Hr/SkillMatrix/SkillMatrixInsert.vue';
import skillmatrixEdit from './views/Hr/SkillMatrix/SkillMatrixEdit.vue';

import settingdepartment from './views/Setting/Setting.vue';

/*  marketing */
import mktcategory from './views/Dashboard/MktCategory.vue';
import marketingenquiry from './views/Marketing/MarketingEnquiry.vue';
import marketingenquiryinsert from './views/Marketing/MarketingEnquiryInsert.vue';
import marketingenquiryList from './views/Marketing/marketingenquiryList.vue';
import marketingEnquiryEdit from './views/Marketing/marketingenquiryEdit.vue';
import ConfigrationManagementList from './views/Marketing/ConfigrationManagementList.vue';
import configurationinsert from './views/Marketing/ConfigurationManagementInsert.vue';
import TechfeasibilityList from './views/Marketing/TechFeasibilityList.vue';
import QualityfeasibilityList from './views/Marketing/QualityFeasibilityList.vue';
import MarketingfeasibilityList from './views/Marketing/MarketingFeasibilityList.vue';
import Reviewer from './views/Marketing/Reviewer.vue';
import feasibilityinsert from './views/Marketing/FeasibilityInsert.vue';
import feasibilitydetail from './views/Marketing/FeasibilityDetail.vue';

// mr
import MrCategory from './views/Dashboard/MrCategory.vue';
import MrDocType from './views/Mr/DocType.vue';


import contractreview from './views/Marketing/ContractReviewDetail.vue';
import contractreviewinsert from './views/Marketing/ContractReviewInsert.vue';
import configurationdetail from './views/Marketing/ConfigurationManagement.vue';
import Treeview from './views/Setting/Treeview.vue';
import masterlist from './views/Master/MasterDetail.vue';
import masterinsert from './views/Master/MasterInsert.vue';
import suplierevaluation from './views/Pur/PurDetail.vue';
import suplierevaluationinsert from './views/Pur/PurInsert.vue';


Vue.use(Router);
export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    { path: '/', name: 'login', component: Login },
    { path: '/dashboard', name: 'home', component: Home },
    { path: '/hr-list', name: 'hrlist', component: Hrlist },
// hr
    { path: '/hr-detail/:id', name: 'Hrdetail', component: Hrdetail },
    { path: '/hr', name: 'subcategory', component: subcategory },
    { path: '/employee', name: 'EmployeeList', component: EmployeeList },
    { path: '/employee/:id', name: 'EmployeeDetail', component: EmployeeDetail },
    { path: '/compentency-matrix', name: 'compentency', component: compentency },
    { path: '/compentency-matrix/:id', name: 'compentencyDetail', component: compentencyDetail },
    { path: '/trining-request-register', name: 'TrainingRequestRegisterList', component: TrrList },
    { path: '/trining-request-register/:id', name: 'TrainingRequestRegisterDetail', component: TrrDetails },
    { path: '/anual-training-plan', name: 'Anual training', component: anualtraing },
    { path: '/anual-training-plan/:id', name: 'Anual training details', component: anualtraingDetails },
    { path: '/training-evalution-record', name: 'Training evalution record', component: trEvalution },
    { path: '/skill-matrix', name: 'Skill matrix list', component: skillmatrix },
    { path: '/skill-matrix/:id', name: 'Skill matrix', component: skillmatrixDetail },
    { path: '/skill-matrix-insert', name: 'Skill matrix insert', component: skillmatrixInsert },
    { path: '/skill-matrix-edit/:id', name: 'Skill matrix edit', component: skillmatrixEdit },
    { path: '/department', name: 'Department', component: settingdepartment },
// mrk
    { path: '/mkt', name: 'Marketing Sub Category', component: mktcategory },
    { path: '/marketing-enquiry', name: 'Marketing Enquiry', component: marketingenquiryList },
    { path: '/marketing-enquiry/:id', name: 'Marketing Enquiry Detail', component: marketingenquiry },
    { path: '/marketing-enquiry-insert', name: 'Marketing Enquiry Insert', component: marketingenquiryinsert },
    { path: '/marketing-enquiry-edit/:id', name: 'Marketing Enquiry edit', component: marketingEnquiryEdit },
    { path: '/technical-feasiblity', name: 'Technical Feasibility List', component: TechfeasibilityList },
    { path: '/quality-feasibility', name: 'Quality Feasibility List', component: QualityfeasibilityList },
    { path: '/marketing-feasibility', name: 'Marketing Feasibility List', component: MarketingfeasibilityList },
    { path: '/reviewer', name: 'Reviewer', component: Reviewer },
    { path: '/configration-management', name: 'Configration Management', component: ConfigrationManagementList },
// settings
    { path: '/feasibility-insert', name: 'Feasibility Insert', component: feasibilityinsert },
    { path: '/contract-review', name: 'Contract Review', component: contractreview },
    { path: '/contract-review-insert', name: 'Contract Review Insert', component: contractreviewinsert },
    { path: '/configuration-management', name: 'Contract Review ', component: configurationdetail },
    { path: '/configration-management-add', name: 'Contract Review Insert', component: configurationinsert },
    { path: '/tree-view', name: 'Tree View', component: Treeview },
    { path: '/master-list', name: 'Master List', component: masterlist },
    { path: '/master-list-insert', name: 'Master List Insert', component: masterinsert },
    { path: '/supplier-evaluation', name: 'Supplier Evaluation', component: suplierevaluation },
    { path: '/supplier-evaluation-insert', name: 'Supplier Evaluation Insert', component: suplierevaluationinsert },
// Mr
    { path: '/mr', name: 'Master List category', component: MrCategory },
    { path: '/mr-doc-type', name: 'MR document type', component: MrDocType },

    
  ],
});

