<template>
  <div>
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">Purchase Order</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right">
          <v-btn-toggle class="transparent mr-2">
            <router-link :to="{ path: '/purchase-order-add'}">
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
        <td class="text-xs-left">
          <router-link :to="{ path: 'purchase-order/'+ props.item.id }">{{ props.item.id }}</router-link>
        </td>
        <td class="text-xs-left">{{ props.item.supplierName }}</td>
        <td class="text-xs-left">{{ props.item.product }}</td>
        <td class="text-xs-left">{{ props.item.unit }}</td>
        <td class="text-xs-left">{{ props.item.supplier_ref_no }}</td>
        <td class="text-xs-left">{{ props.item.qty }}</td>
        <td class="text-xs-left">{{ props.item.po_no }}</td>
        <td class="text-xs-left">{{ props.item.po_date }}</td>
        <td class="text-xs-left">{{ props.item.requested_date }}</td>
        <td class="text-xs-left">
          <router-link :to="{ path: 'purchase-order/' + props.item.id }">
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
        {
          text: "SL NO",
          align: "left",
          value: "id"
        },
        { text: "Supplier", value: "supplierName" },
        { text: "Product", value: "product" },
        { text: "Unit", value: "unit" },
        { text: "Supplier ref no ", value: "supplier_ref_no" },
        { text: "Qty", value: "qty" },
        { text: "Po no ", value: "po_no" },
        { text: "Po date ", value: "po_date" },
        { text: "Requested date ", value: "requested_date" },
        { text: "Status", value: "status" }
      ],
      tlist: []
    };
  },

  mounted() {
    this.getall();
  },

  methods: {
    getall() {
      var self = this;
      axios
        .get(this.$apiUrl + "pur/purchase-order/")
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
            .delete(this.$apiUrl + "pur/purchase-order/" + did)
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
