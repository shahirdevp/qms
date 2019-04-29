<template>
  <div>
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">TECHNICAL FEASIBLITY</h3>
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
          <router-link :to="{ path: 'technicall-feasiblity/'+ props.item.id }">{{ props.item.cusomer }}</router-link>
        </td>
        <td class="text-xs-left">{{ props.item.r_mtrl === '1' ? 'Yes':'No' }}</td>
        <td class="text-xs-left">{{ props.item.m_c === '1' ? 'Yes':'No' }}</td>
        <td class="text-xs-left">{{ props.item.tools === '1' ? 'Yes':'No' }}</td>
        <td class="text-xs-left">{{ props.item.Spl_process === '1' ? 'Yes':'No' }}</td>
        <td class="text-xs-left">{{ props.item.any_cad_req === '1' ? 'Yes':'No' }}</td>
        <td class="text-xs-left">{{ props.item.out_source === '1' ? 'Yes':'No' }}</td>
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
          value: "cusomer"
        },
        { text: "R/Mtrl", value: "r_mtrl" },
        { text: "M/c", value: "m_c" },
        { text: "Tools", value: "tools" },
        { text: "Spl. Process", value: "Spl_process" },
        { text: "Any CAD req?", value: "any_cad_req" },
        { text: "Out source?", value: "out_source" }
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
        .get(this.$apiUrl + "mkt/technicall-feasiblity/")
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
