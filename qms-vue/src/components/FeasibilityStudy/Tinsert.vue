<template>
  <div id="empd">
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">Feasibility Study</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right"></div>
      </v-flex>
    </v-layout>

    <!-- Insert-list-form -->

    <div class="card-box">
        <div class="insert-table-box">
            <table class="insert-table">
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
                      <textarea name="" id=""  rows="1" class="table-input"></textarea>
                  </td>
                  <td>
                      <textarea name="" id=""  rows="1" class="table-input"></textarea>
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
        { slno:"4", capability:'Manufacturing Milling', reqname:'', reamarkname:'', isheading:false },
        { slno:"4.1", capability:'Maximum Length', reqname:'', reamarkname:'', isheading:false },
        { slno:"4.2", capability:'Minimum length', reqname:'', reamarkname:'', isheading:false },
        { slno:"4.3", capability:'Height', reqname:'', reamarkname:'', isheading:false },
        { slno:"4.5", capability:'Maximum Tool', reqname:'', reamarkname:'', isheading:false },
        { slno:"4.6", capability:'Achieving the specified tolerance &  accordance', reqname:'', reamarkname:'', isheading:false },
      ]
    };
  }
};
</script>

<style scoped>
.insert-table-box .insert-table thead th:nth-child(1){ max-width: 75px; }
.insert-table-box .insert-table thead th:nth-child(2){ max-width:32%; width:32%; }
.insert-table-box .insert-table thead th:nth-child(3){ max-width:calc(33% - 25px); }
.insert-table-box .insert-table thead th:nth-child(4){ width:calc(33% - 25px); }
.insert-table-box .insert-table, .insert-table-box .insert-table td, .insert-table-box .insert-table th {   border: 1px solid black;   border-collapse: collapse; }
.insert-table-box .insert-table td, .insert-table-box .insert-table th{padding: 8px}
.insert-table-box .insert-table textarea{width:100%}
.insert-table-box .insert-table .t-head{ background: #4b83cc; color: #fff; }
</style>









