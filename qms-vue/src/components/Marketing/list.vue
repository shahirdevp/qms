<template>
  <div>
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">MARKETING ENQUIRY REGISTER</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right">
          <router-link :to="'marketing-enquiry-insert'">
            <v-btn color="primary" ref="fileInput">
              Add New
              <v-icon right>add</v-icon>
            </v-btn>
          </router-link>
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
          <router-link :to="{ path: 'marketing-enquiry/'+ props.item.id }">{{ props.item.customer }}</router-link>
        </td>
        <td class="text-xs-left">{{ props.item.contact }}</td>
        <td class="text-xs-left">{{ props.item.line_number }}</td>
        <td class="text-xs-left">{{ props.item.partNumber }}</td>
        <td class="text-xs-left">{{ props.item.qty }}</td>
        <td class="text-xs-left">{{ props.item.drawingNumber }}</td>
        <td class="text-xs-left">{{ props.item.date }}</td>
        <td class="text-xs-left">{{ props.item.status }}</td>
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
        { text: "Contact", value: "contact" },
        { text: "Line No", value: "line_number" },
        { text: "Part Number", value: "partNumber" },
        { text: "Qty", value: "qty" },
        { text: "Drawing Number", value: "drawingNumber" },
        { text: "Date", value: "date" },
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
        .get(this.$apiUrl + "mkt/enquery-register/")
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
