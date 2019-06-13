<template>
  <div>
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">Internal Audit Report</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right">
          <v-btn-toggle class="transparent mr-2">
            <router-link :to="{ path: '/mr-non-conformance-add'}">
              <v-btn flat value="right">
                <v-icon color="info">add</v-icon>
                <span>Add New</span>
              </v-btn>
            </router-link>
          </v-btn-toggle>
        </div>
      </v-flex>
    </v-layout>

    <v-data-table
      :headers="headers"
      :items="tlist"
      class="elevation-1"
      :rows-per-page-items="[10,20,50]"
    >
      <template v-slot:items="props">
        <td class="text-xs-left">{{ props.item.id }}</td>
        <td class="text-xs-left">{{ props.item.area_of_audit }}</td>
        <td class="text-xs-left">{{ props.item.ncr_no}}</td>
        <td class="text-xs-left">{{ props.item.nc_statement }}</td>
        <td class="text-xs-left">{{ props.item.objective_evidence }}</td>
        <td class="text-xs-left">{{ props.item.containment_action }}</td>
        <td class="text-xs-left">{{ props.item.correction }}</td>
        <td class="text-xs-left">{{ props.item.root_cause }}</td>
        <td class="text-xs-left">{{ props.item.correction_action }}</td>
        <td class="text-xs-left">
          <router-link :to="{ path: '/mr-non-conformance/' + props.item.id }">
            <v-icon small class="mr-3" color="info">visibility</v-icon>
          </router-link>
          <v-icon small color="red" @click="deleteData(props.item.id)">delete</v-icon>
        </td>
      </template>
    </v-data-table>
  </div>
</template>

<script>
import axios from "axios";
import swal from "sweetalert2";
import router from "../../router";

export default {
  data() {
    return {
      // table ist
      headers: [
        { text: "SL NO ", align: "left", value: "id" },
        { text: "Area of Audit", value: "area_of_audit" },
        { text: "Ncr no", value: "ncr_no" },
        { text: "Nc statement", value: "nc_statement" },
        { text: "Objective evidence", value: "objective_evidence" },
        { text: "Containment action", value: "containment_action" },
        { text: "Correction", value: "correction" },
        { text: "Root cause", value: "root_cause" },
        { text: "Correction action ", value: "correction_action" },
        { text: "Action", value: "" }
      ],
      tlist: [],
    };
  },
  mounted() {
    this.getall();
  },
  methods: {
    getall() {
      var self = this;
      axios
        .get(this.$apiUrl + "mr/non-conf/")
        .then(function(response) {
          self.tlist = response.data;
        })
        .catch(function(error) {
          console.log(error.data);
        });
    },
    deleteData(did) {
      var self = this;

      swal({
        title: "Are you sure?",
        text: "You won't be able to revert this!",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes, delete it!"
      }).then(result => {
        if (result.value) {
          axios
            .delete(this.$apiUrl + "mr/non-conf/" + did)
            .then(function(response) {
              swal({
                title: "Success",
                text: "Successfully Delete",
                type: "success",
                showConfirmButton: false,
                showCloseButton: false,
                timer: 3000
              });
              self.getall();
            })
            .catch(function(error) {
              swal({
                type: "error",
                title: "Oops...",
                text: "Something went wrong!",
                showConfirmButton: false,
                showCloseButton: false,
                timer: 3000
              });
            });
        }
      });
    }
  }
};
</script>
