<template>
  <div id="empd">
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">Feasibility Study</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right">
          <div>All changes saved

              <v-progress-circular
              :width="2"
              color="blue darken-3"
              indeterminate
              size="20"
            ></v-progress-circular>
          </div>
        </div>
      </v-flex>
    </v-layout>
    <!-- Insert-list-form -->

    <div class="card-box">
        <div id="loder-container" :class="{'dnon': dnon}"> 
          <v-progress-circular
                :width="4"
                color="blue darken-3"
                indeterminate
                size="50"
            ></v-progress-circular>
        </div>
        <div class="insert-table-box">

            <table class="insert-table customer-table">
                <tr>
                  <th>Customer Name</th>
                  <td>
                    <div class="select-form">
                        <select name=""  @change="selectedCustomer()" id="" v-model="slectCustomer">
                            <option value="">Choose Customer</option>
                            <option v-for="customer in customers" :key="customer.id" :value="customer.id">{{ customer.customer }}</option>
                        </select>
                    </div>
                    
                  </td>

                  <th>Customer Part</th>
                  <td>
                      <!-- <div class="select-form">
                      <select name="" id="" >
                          <option value="">Customer Part 1</option>
                          <option value="">Customer Part 2</option>
                          <option value="">Customer Part 3</option>
                          <option value="">Customer Part 4</option>
                        </select>
                      </div> -->
                      {{selectedCustomers.quotationRef}}
                      <input type="hidden"  >
                  </td>
                  
                </tr>

                <tr>
                  
                  <th>Customer Reference</th>
                  <td>{{ selectedCustomers.quotationRef }}</td>
                  <th>Description</th>
                  <td>{{ selectedCustomers.description }}</td>
                </tr>
            </table>  

            <table class="insert-table customer-table2" >
              <tr>
                <th>
                  Statutory & Regulatory Requirement
                </th>
                <td>
                    <textarea name="" id="" v-model="statutory"  rows="1" class="table-input"></textarea>
                </td>
              </tr>
            </table> 

            <table class="insert-table customer-table3">
              <thead>
                <tr>
                  <th>SL NO</th>
                  <th>Company Capability</th>
                  <th>Customer Requirement</th>
                  <th>Remarks</th>
                </tr>
              </thead>

              <tbody>
                <tr v-for="item in tbdata" >
                  <td :class="{'t-head': item.isheading}">{{ item.slno }}</td>
                  <td :class="{'t-head': item.isheading}">{{ item.capability }}</td>
                  <td>
                      <textarea name="" @change="uploadData()" id="" v-model="item.reqname" rows="1" class="table-input"></textarea>
                  </td>
                  <td>
                      <textarea name="" @change="uploadData()" id=""  v-model='item.reamarkname' rows="1" class="table-input"></textarea>
                  </td>
                </tr>
              </tbody>
            </table>
        </div>
    </div>
  </div>
</template>

<script>
import swal from "sweetalert2";
import router from "../../router";

export default {
  data() {
    return {
      tbdata:[
        { slno:"1", capability:'Drawing Dimensional review', reqname:'', reamarkname:'', isheading:true },
        { slno:"1.1", capability:'Check and confirm Manufacturing feasibility for all linear, Angular and profile dimensions', reqname:'', reamarkname:'', isheading:false },
        { slno:"1.2", capability:'Identify all GD&T features and manufacturing feasibility', reqname:'', reamarkname:'', isheading:false },
        { slno:"1.3", capability:'Identify all true position requirements and Manufacturing feasibility', reqname:'', reamarkname:'', isheading:false },
        { slno:"1.4", capability:'Identify all Major characteristics and measurement methods', reqname:'', reamarkname:'', isheading:false },
        { slno:"1.5", capability:'Identify all Minor characteristics and measurement methods', reqname:'', reamarkname:'', isheading:false },
        { slno:"1.6", capability:'Identify all Key characteristics on the drawing with Measurement and control methods', reqname:'', reamarkname:'', isheading:false },
        { slno:"2", capability:'DRAWING STANDRED', reqname:'', reamarkname:'', isheading:true },
        { slno:"2.1", capability:'Verify The Drawing', reqname:'', reamarkname:'', isheading:false },
        { slno:"3", capability:'Manufacturing Turing', reqname:'', reamarkname:'', isheading:true },
        { slno:"3.1", capability:'Maximum Dia for Machine', reqname:'', reamarkname:'', isheading:false },
        { slno:"3.2", capability:'Minimum Dia for Machine', reqname:'', reamarkname:'', isheading:false },
        { slno:"3.3", capability:'Maximum Length', reqname:'', reamarkname:'', isheading:false },
        { slno:"3.4", capability:'Minimum Length', reqname:'', reamarkname:'', isheading:false },
        { slno:"3.5", capability:'Achieving the specified tolerance &  accordance', reqname:'', reamarkname:'', isheading:false },
        { slno:"4", capability:'Manufacturing Milling', reqname:'', reamarkname:'', isheading:true },
        { slno:"4.1", capability:'Maximum Length', reqname:'', reamarkname:'', isheading:false },
        { slno:"4.2", capability:'Minimum length', reqname:'', reamarkname:'', isheading:false },
        { slno:"4.3", capability:'Height', reqname:'', reamarkname:'', isheading:false },
        { slno:"4.4", capability:'Maximum Tool', reqname:'', reamarkname:'', isheading:false },
        { slno:"4.5", capability:'Achieving the specified tolerance &  accordance', reqname:'', reamarkname:'', isheading:false },
      ],
      customers:[],
      slectCustomer:'',
      dnon:true,
      selectedCustomers:[],
      statutory:'',
    };
  },
  mounted() {
    this.getcustomer();
  },
  methods: {
    // get customer list
    getcustomer(){
      var self = this;
      axios.get(this.$apiUrl+'mkt/customer-list/', {
        
      })
      .then(function (response) {
        self.customers = response.data;
      })
      .catch(function (error) {
      })
    },
    // get customer data
    selectedCustomer(){
      if(!this.slectCustomer == ''){
        this.dnon = false;
        var self = this;
        axios.get(this.$apiUrl+'mkt/enquery-register/'+ this.slectCustomer + '/', {})
        .then(function (response){
          self.dnon = true;
          self.selectedCustomers = response.data
        }).catch(function(error){

        })
      }
    },
    uploadData(){
      axios.post(this.$apiUrl+'mkt/feasiblity-study/', {
        statutory: this.statutory,
        customer: this.slectCustomer,
        feasibility_study_list:this.tbdata,
        owner:this.$owner
      })
      .then(function (response) {
        console.log(response.data);
        
      })
      .catch(function (error) {
      })
    }


  }
};
</script>

<style scoped>
.insert-table-box .insert-table thead th:nth-child(1){ max-width: 75px; }
.insert-table-box .insert-table thead th:nth-child(2){ max-width:32%; width:32%; }
.insert-table-box .insert-table thead th:nth-child(3){ max-width:calc(33% - 25px); }
.insert-table-box .insert-table thead th:nth-child(4){ width:calc(33% - 25px); }
.insert-table-box .insert-table, .insert-table-box .insert-table td, .insert-table-box .insert-table th {   border: 1px solid #8f8f8f;   border-collapse: collapse; }
.insert-table-box .insert-table td{padding: 2px}
.insert-table-box .insert-table th{padding: 8px;background:#f8f8f8}
.insert-table-box .insert-table textarea{width:100%}
.insert-table-box .insert-table .t-head{ background: #4b83cc; color: #fff; }
.insert-table-box{overflow: auto; height: calc(100vh - 194px); scrollbar-width: thin;}
.insert-table-box .insert-table{width: 100%; margin-bottom: 10px;border-radius: 3px}
.insert-table-box .customer-table tr td, .insert-table-box .customer-table tr th{width:25%}
.insert-table-box .customer-table2 tr th{width:25%}
.insert-table-box .customer-table tr td select{width: 100%}
.select-form:after{ content: ""; position: absolute; right: 4px; top: 9px; border-left: 5px solid #0000; border-right: 5px solid #0000; border-top: 7px solid #292d29; border-bottom: transparent; }
.select-form{position: relative;}
#loder-container{position: absolute; width: 100%; left: 0; height: 100%; background: #00000012; top: 0;z-index: 99;}
.v-progress-circular { position: absolute; left: 0; top: 0; right: 0; bottom: 0; margin: auto; }
.dnon{display:none}
</style>









