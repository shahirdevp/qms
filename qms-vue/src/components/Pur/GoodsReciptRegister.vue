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
          <router-link :to="{ path: 'marketing-enquiry/'+ props.item.id }">{{ props.item.id }}</router-link>
        </td>
        <td class="text-xs-left">{{ props.item.grrno }}</td>
        <td class="text-xs-left">{{ props.item.date }}</td>
        <td class="text-xs-left">{{ props.item.supplier }}</td>
        <td class="text-xs-left">{{ props.item.dc_ref }}</td>
        <td class="text-xs-left">{{ props.item.po_ref }}</td>
        <td class="text-xs-left">{{ props.item.part }}</td>
        <td class="text-xs-left">{{ props.item.inward_qty }}</td>
        <td class="text-xs-left">{{ props.item.sup_test_report }}</td>
        <td class="text-xs-left">{{ props.item.heat_lot_no }}</td>
        <td class="text-xs-left">{{ props.item.lenght }}</td>
        <td class="text-xs-left">{{ props.item.Hieght }}</td>
        <td class="text-xs-left">{{ props.item.width }}</td>
        <td class="text-xs-left">{{ props.item.diameter }}</td>
        <td class="text-xs-left">{{ props.item.rej_qty }}</td>
        <td class="text-xs-left">{{ props.item.return_dc }}</td>
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
      // table ist
      headers: [
        {
          text: "SL NO",
          align: "left",
          value: "id"
        },
        { text: "GRR No", value: "grrno" },
        { text: "Date", value: "date" },
        { text: "Supplier", value: "supplier" },
        { text: "Dc ref ", value: "dc_ref" },
        { text: "Po ref", value: "po_ref" },
        { text: "Part", value: "part" },
        { text: "Inward Qty", value: "inward_qty" },
        { text: "Sup test report", value: "sup_test_report" },
        { text: "Heat lot no", value: "heat_lot_no" },
        { text: "Lenght", value: "lenght" },
        { text: "Hieght", value: "Hieght" },
        { text: "Width", value: "width" },
        { text: "Diameter", value: "diameter" },
        { text: "Accepted Qty", value: "accepted_qty" },
        { text: "Rej. Qty", value: "rej_qty" },
        { text: "Return DC", value: "return_dc" },
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
        .get(this.$apiUrl + "pur/goods-recipt/")
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
            .delete(this.$apiUrl + "pur/goods-recipt/" + did)
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
