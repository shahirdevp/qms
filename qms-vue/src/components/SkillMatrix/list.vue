<template>
  <div>
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">SKILL MATRIX</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right">
          <v-btn color="primary" ref="fileInput">
            Add New
            <v-icon right>add</v-icon>
          </v-btn>
        </div>
      </v-flex>
    </v-layout>

    <v-data-table
      :headers="headers"
      :items="info"
      class="elevation-1"
      :rows-per-page-items="[10,20,50]"
    >
      <template v-slot:items="props">
        <td class="text-xs-left">
          <router-link :to="{ path: 'skill-matrix/'+ props.item.id }" >{{ props.item.id }}</router-link>
        </td>
        <td class="text-xs-left"><router-link :to="{ path: 'skill-matrix/'+ props.item.id }" >{{ props.item.depaertment }}</router-link></td>
        <td class="text-xs-left">{{ props.item.designation }}</td>
        <td class="text-xs-left">{{ props.item.created_On }}</td>
        <td class="text-xs-left">{{ props.item.prepredBy }}</td>
        <td class="text-xs-left">{{ props.item.approvedBy }}</td>
      </template>
    </v-data-table>
  </div>

  <!-- 
    # Fetch hr lis - api - http://localhost:8000/api/v1/hr/
    #add new post - component - addPost
  -->
</template>

			
<script>
import axios from "axios";
import swal from "sweetalert2";
import router from "../../router";

export default {
  data() {
    return {
      drawer: null,
      // table ist
      headers: [
        { text: "ID", align: "left", value: "id" },
        { text: "Department", value: "depaertment" },
        { text: "Designation", value: "designation" },
        { text: "Date", value: "created_On" },
        { text: "Prepard By", value: "prepredBy" },
        { text: "Approved By", value: "approvedBy" },
      ],
      info: [],
    };
  },

  mounted() {
    this.getall();
  },

  methods: {
    getall() {
      var self = this;
      axios
        .get(this.$apiUrl+'skill-matrix/')
        .then(function(response) {
          self.info = response.data;
        })
        .catch(function(error) {
          console.log(error);
        });
    },  
  }
};
</script>

