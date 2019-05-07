<template>
  <div>
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">Suppliers List</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right">
          <v-btn-toggle class="transparent mr-2">
            <router-link :to="{ path: '/suppliers-add'}">
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
        <td class="text-xs-left">{{ props.item.supplier }}</td>
        <td class="text-xs-left">{{ props.item.email}}</td>
        <td class="text-xs-left">{{ props.item.phone }}</td>
        <td class="text-xs-left">{{ props.item.website }}</td>
        <td class="text-xs-left">{{ props.item.country }}</td>
        <td class="text-xs-left">{{ props.item.state }}</td>
        <td class="text-xs-left">{{ props.item.city }}</td>
        <td class="text-xs-left">{{ props.item.street }}</td>
        <td class="text-xs-left">{{ props.item.pin }}</td>
        <td class="text-xs-left">
          <router-link :to="{ path: '/suppliers/' + props.item.id }">
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
      headers: [
        { text: "SL NO ", align: "left", value: "id" },
        { text: "Supplier", value: "supplier" },
        { text: "Email", value: "email" },
        { text: "Phone", value: "phone" },
        { text: "Website", value: "website" },
        { text: "Country", value: "country" },
        { text: "State", value: "state" },
        { text: "City", value: "city" },
        { text: "Street ", value: "street" },
        { text: "Pin ", value: "pin" },
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
        .get(this.$apiUrl + "pur/supplier/")
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
            .delete(this.$apiUrl + "pur/supplier/" + did)
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
