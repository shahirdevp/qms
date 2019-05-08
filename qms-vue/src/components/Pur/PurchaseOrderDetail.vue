<template>
  <div class>
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <v-btn-toggle class="transparent">
            <router-link :to="{ path: './'}" replace>
              <v-btn flat value="right">
                <v-icon >keyboard_backspace</v-icon>
                <span class="ml-1">Back</span>
              </v-btn>
            </router-link>
          </v-btn-toggle>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right">
          <v-btn-toggle class="transparent">
            <router-link :to="{ path: '../purchase-order-edit/' + detail.id }" replace>
              <v-btn flat value="left">
                <span>Edit</span>
                <v-icon color="info">edit</v-icon>
              </v-btn>
            </router-link>
            <v-btn @click="deleteData()" flat value="center">
              <span>Delete</span>
              <v-icon color="red">delete</v-icon>
            </v-btn>
          </v-btn-toggle>
        </div>
      </v-flex>
    </v-layout>
    <!-- detail -->
    <v-layout>
      <v-flex xs12 sm12 md10 >
            <v-card class="mt-3 ml-3 mr-3 custom-card-list">
                <v-card-text>
                    <table class="card-table">
                      <tr>
                        <td>
                          <h3 class="mb-3" color="black">Purchase Order</h3>
                        </td>
                      </tr>
                      <tr>
                        <th>Supplier</th>
                        <td>{{ detail.supplier }}</td>
                      </tr>
                      <tr>
                        <th>Product</th>
                        <td>{{ detail.product }}</td>
                      </tr>
                      <tr>
                        <th>Unit</th>
                        <td>{{ detail.unit }}</td>
                      </tr>
                      <tr>
                        <th>Supplier ref no </th>
                        <td>{{ detail.supplier_ref_no }}</td>
                      </tr>
                      <tr>
                        <th>Qty</th>
                        <td>{{ detail.qty }}</td>
                      </tr>
                      <tr>
                        <th>Po no</th>
                        <td>{{ detail.po_no }}</td>
                      </tr>
                      <tr>
                        <th>Po date</th>
                        <td>{{ detail.po_date }}</td>
                      </tr>
                      <tr>
                        <th>Requested date</th>
                        <td>{{ detail.requested_date }}</td>
                      </tr>
                    </table>
                   
                </v-card-text>
            </v-card>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import swal from "sweetalert2";
import router from "../../router";

export default {
  data() {
    return {
      detail: []
    };
  },
  mounted() {
    this.getdetails();
  },
  computed: {},
  methods: {
    getdetails() {
      var ts = window.location.pathname.split("/");
      var parQuery = ts[ts.length - 1];
      var self = this;
      axios
        .get(this.$apiUrl + "pur/purchase-order/" + parQuery + '/')
        .then(function(response) {
          self.detail = response.data;
        })
        .catch(function(error) {
          console.log(error.data);
        });
    },

    deleteData() {
      var ts = window.location.pathname.split("/");
      var parQuery = ts[ts.length - 1];
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
            .delete(this.$apiUrl + "pur/purchase-order/" + parQuery + '/')
            .then(function(response) {
              swal({
                title: "Success",
                text: "Successfully Delete",
                type: "success",
                showConfirmButton: false,
                showCloseButton: false,
                timer: 3000
              });
              router.push("/suppliers");
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









