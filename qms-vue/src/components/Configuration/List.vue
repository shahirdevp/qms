<template>
  <div>
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">Configration Management</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right">
          <v-btn-toggle class="transparent mr-2" >
            <router-link :to="{ path: '/configration-management-add'}" >
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
          <router-link :to="{ path: 'configration-management/'+ props.item.id }">{{ props.item.cusomer }}</router-link>
        </td>
        <td class="text-xs-left">{{ props.item.customer_order }}</td>
        <td class="text-xs-left">{{ props.item.route_card_no }}</td>
        <td class="text-xs-left">{{ props.item.internal_job_order }}</td>
        <td class="text-xs-left">{{ props.item.rev_no }}</td>
        <td class="text-xs-left">{{ props.item.invoice_no }}</td>
        <td class="text-xs-left">{{ props.item.creadedOn }}</td>
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
          text: "Customer",
          align: "left",
          value: "customer"
        },
        { text: "Customer Order", value: "customer_order" },
        { text: "Route Card No", value: "route_card_no" },
        { text: "Internal Job Order", value: "internal_job_order" },
        { text: "Rev. No", value: "rev_no" },
        { text: "Invoice No", value: "invoice_no" },
        { text: "Date", value: "creadedOn" }
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
        .get(this.$apiUrl + "mkt/configuration-management-report/")
        .then(function(response) {
          self.tlist = response.data;
        })
        .catch(function(error) {
          console.log(error.data);
        });
    }
  }
};
</script>
