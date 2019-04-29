<template>
  <div>
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">TECHNICAL FEASIBLITY</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right">
          <v-dialog v-model="dialog" max-width="500px">
            <template v-slot:activator="{ on }">
              <v-btn color="primary" dark class="mb-2" v-on="on">New Item</v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="headline">{{ formTitle }} TECHNICAL FEASIBLITY</span>
              </v-card-title>

              <v-card-text>
                <v-container grid-list-md>
                  <v-layout wrap>
                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="tlist.cusomer" label="Customer"></v-text-field>
                    </v-flex>
                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="tlist.r_mtrl" label="R/Mtrl"></v-text-field>
                      <!-- <v-select
                        v-model="select"
                        :options="options"
                         item-text="text"
                         item-value="value"
                        label="R/Mtrl"
                      ></v-select> -->
                    </v-flex>
                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="tlist.m_c" label="M/c"></v-text-field>
                    </v-flex>
                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="tlist.tools" label="Tools"></v-text-field>
                    </v-flex>
                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="tlist.Spl_process" label="Spl. Process"></v-text-field>
                    </v-flex>
                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="tlist.any_cad_req" label="Any CAD req?"></v-text-field>
                    </v-flex>
                    <v-flex xs12 sm6 md>
                      <v-text-field v-model="tlist.out_source" label="Out source?"></v-text-field>
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
        <td class="text-xs-left">{{ props.item.r_mtrl === '1' ? 'Yes':'No' }}</td>
        <td class="text-xs-left">{{ props.item.m_c === '1' ? 'Yes':'No' }}</td>
        <td class="text-xs-left">{{ props.item.tools === '1' ? 'Yes':'No' }}</td>
        <td class="text-xs-left">{{ props.item.Spl_process === '1' ? 'Yes':'No' }}</td>
        <td class="text-xs-left">{{ props.item.any_cad_req === '1' ? 'Yes':'No' }}</td>
        <td class="text-xs-left">{{ props.item.out_source === '1' ? 'Yes':'No' }}</td>
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
        { text: "R/Mtrl", value: "r_mtrl" },
        { text: "M/c", value: "m_c" },
        { text: "Tools", value: "tools" },
        { text: "Spl. Process", value: "Spl_process" },
        { text: "Any CAD req?", value: "any_cad_req" },
        { text: "Out source?", value: "out_source" },
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
      defaultItem: {
        cusomer: "",
        r_mtrl: "",
        m_c: "",
        Spl_process: "",
        any_cad_req: "",
        out_source: "",
        tools: ""
      }
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
        .get(this.$apiUrl + "mkt/technicall-feasiblity/")
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
            .delete(this.$apiUrl + "mkt/technicall-feasiblity/" + did)
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
        axios.post(this.$apiUrl+'mkt/technicall-feasiblity/', {
            cusomer: this.tlist.cusomer,
            r_mtrl : this.tlist.r_mtrl,
            m_c : this.tlist.m_c,
            tools : this.tlist.tools,
            Spl_process : this.tlist.Spl_process,
            any_cad_req : this.tlist.any_cad_req,
           out_source : this.tlist.out_source,
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
      setTimeout(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      }, 300);
    }
  }
};
</script>
