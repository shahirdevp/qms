<template>
  <div>
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">Stock Register</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right">
          <v-btn-toggle class="transparent mr-2">
            <router-link :to="{ path: '/stock-register-add'}">
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
        <td class="text-xs-left">{{ props.item.part_no }}</td>
        <td class="text-xs-left">{{ props.item.description}}</td>
        <td class="text-xs-left">{{ props.item.doc_ref }}</td>
        <td class="text-xs-left">{{ props.item.detail }}</td>
        <td class="text-xs-left">{{ props.item.recipt }}</td>
        <td class="text-xs-left">{{ props.item.issue }}</td>
        <td class="text-xs-left">{{ props.item.balance }}</td>
        <td class="text-xs-left">{{ props.item.date }}</td>
        <td class="text-xs-left">
          <router-link :to="{ path: '/stock-register-edit/' + props.item.id }">
            <v-icon small class="mr-3" color="info">edit</v-icon>
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
      headers: [
        { text: "SL NO ", align: "left", value: "id" },
        { text: "Part no", value: "part_no" },
        { text: "Description ", value: "description" },
        { text: "Doc ref", value: "doc_ref" },
        { text: "Detail", value: "detail" },
        { text: "Recipt ", value: "recipt" },
        { text: "Issue ", value: "issue" },
        { text: "Balance", value: "balance" },
        { text: "Date ", value: "date" },
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
        .get(this.$apiUrl + "pur/stock-register/")
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
            .delete(this.$apiUrl + "pur/stock-register/" + did)
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
