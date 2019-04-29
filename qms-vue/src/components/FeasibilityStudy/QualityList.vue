<template>
  <div>
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">Quality  Feasibility</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right">
          <v-dialog v-model="dialog" max-width="500px">
            <template v-slot:activator="{ on }">
              <v-btn color="primary" dark class="mb-2" v-on="on">New Item</v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="headline">{{ formTitle }} Quality  Feasibility</span>
              </v-card-title>

              <v-card-text>
                <v-container grid-list-md>
                  <v-layout wrap>
                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="tlist.cusomer" label="Customer"></v-text-field>
                    </v-flex>
                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="tlist.inst" label="Inst"></v-text-field>
                      <!-- <v-select
                        v-model="select"
                        :options="options"
                         item-text="text"
                         item-value="value"
                        label="R/Mtrl"
                      ></v-select> -->
                    </v-flex>
                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="tlist.gauge" label="Gauge"></v-text-field>
                    </v-flex>
                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="tlist.can_aql_be_achived" label="Is FAI required?"></v-text-field>
                    </v-flex>
                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="tlist.is_fai_required" label="Key chare *"></v-text-field>
                    </v-flex>
                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="tlist.key_chare" label="Can AQL be achived?"></v-text-field>
                    </v-flex>
                    <v-flex xs12 sm6 md>
                      <v-text-field v-model="tlist.ispection_as_per" label="Ispection as per ?"></v-text-field>
                    </v-flex>
                  </v-layout>
                </v-container>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" flat @click="close">Cancel</v-btn>
                <v-btn color="blue darken-1" flat @click="save">Save</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
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
          <router-link
            :to="{ path: 'technical-feasiblity/'+ props.item.id }"
          >{{ props.item.cusomer }}</router-link>
        </td>
        <td class="text-xs-left">{{ props.item.inst === '1' ? 'Yes':'No' }}</td>
        <td class="text-xs-left">{{ props.item.gauge === '1' ? 'Yes':'No' }}</td>
        <td class="text-xs-left">{{ props.item.can_aql_be_achived === '1' ? 'Yes':'No' }}</td>
        <td class="text-xs-left">{{ props.item.is_fai_required === '1' ? 'Yes':'No' }}</td>
        <td class="text-xs-left">{{ props.item.key_chare === '1' ? 'Yes':'No' }}</td>
        <td class="text-xs-left">{{ props.item.ispection_as_per === '1' ? 'Yes':'No' }}</td>
        <td class="text-xs-left">
          <v-icon small class="mr-3" color="info" @click="editItem(props.item)">edit</v-icon>
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
          text: "Customer",
          align: "left",
          value: "cusomer"
        },
        { text: "Inst", value: "r_mtrl" },
        { text: "Gauge", value: "m_c" },
        { text: "Is FAI required?", value: "tools" },
        { text: "Key chare *", value: "Spl_process" },
        { text: "Can AQL be achived?", value: "any_cad_req" },
        { text: "Ispection as per ?", value: "out_source" },
        { text: "Action", value: "" }
      ],
      select: null,
      options: [
        { text: "Yes", value: "0" },
        { text: "NO", value: "1" },
      ],
      tlist: [],

      dialog: false,

      editedIndex: -1,
      editedItem: {
        cusomer: "",
        r_mtrl: "",
        m_c: "",
        Spl_process: "",
        any_cad_req: "",
        out_source: "",
        tools: ""
      },
      
    };
  },

  mounted() {
    this.getall();
  },
  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New " : "Edit ";
    }
  },

  watch: {
    dialog(val) {
      val || this.close();
    }
  },
  methods: {
    getall() {
      var self = this;
      axios
        .get(this.$apiUrl + "mkt/quality-feasibility/")
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
            .delete(this.$apiUrl + "mkt/quality-feasibility/" + did +'/')
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
    },

    editItem(item) {
      this.editedIndex = this.tlist.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.tlist[this.editedIndex], this.editedItem);
      } else {
        var self = this;
        axios.post(this.$apiUrl+'mkt/quality-feasibility/', {
            cusomer: this.tlist.cusomer,
            inst : this.tlist.inst,
            gauge : this.tlist.gauge,
            can_aql_be_achived : this.tlist.can_aql_be_achived,
            is_fai_required : this.tlist.is_fai_required,
            key_chare : this.tlist.key_chare,
           ispection_as_per : this.tlist.ispection_as_per,
           owner : this.$owner,
        })
        .then(function (response) {
          self.getall();
        })
        .catch(function (error) {
            console.log(error);
        });
      }
      this.close();
    },

    close() {
      this.dialog = false;
      
    }
  }
};
</script>
