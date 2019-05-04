<template>
  <div>
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">Internal Audit Report</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right">
          <v-dialog v-model="dialog" max-width="500px">
            <template v-slot:activator="{ on }">
              <v-btn-toggle class="transparent mr-2">
                  <v-btn flat  v-on="on" value="right">
                    <v-icon color="info">add</v-icon>
                    <span>Add New</span>
                  </v-btn>
              </v-btn-toggle>
            </template>
            <v-card>
              <v-card-title>
                <span class="headline">{{ formTitle }} Internal Audit Report</span>
              </v-card-title>

              <v-card-text>
                <v-container grid-list-md>
                  <v-layout wrap>
                    <v-flex xs12>
                      <v-select
                        v-model="tlist.area_of_audit"
                        :items="areaOfAudit"
                        item-text="area_of_audit"
                        item-value="id"
                        label="Area of Audit"
                      ></v-select>
                    </v-flex>
                    <v-flex xs12>
                      <v-text-field v-model="tlist.audit_check_point" label="Audit check point "></v-text-field>
                    </v-flex>
                    <v-flex xs12>
                      <v-text-field v-model="tlist.observations" label="Observations"></v-text-field>
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
        <td class="text-xs-left">{{ props.item.id }}</td>
        <td class="text-xs-left">{{ props.item.area_of_audit.area_of_audit }}</td>
        <td class="text-xs-left">{{ props.item.audit_check_point}}</td>
        <td class="text-xs-left">{{ props.item.observations }}</td>
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
        { text: "SL NO ", align: "left", value: "id" },
        { text: "Area of Audit", value: "area_of_audit.area_of_audit" },
        { text: "Audit Check Point ", value: "audit_check_point" },
        { text: "Observations", value: "observations" },
        { text: "Action", value: "" }
      ],
    
      tlist: [],
      areaOfAudit:[],
      dialog: false,
      editedIndex: -1,
      editedItem: {
        doc_number: "",
        doc_name: "",
        doc_type: "",
        rev_no: "",
        doc_status: ""
      }
    };
  },
  mounted() {
    this.getall();
    this.getAreaofAudit();
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
        .get(this.$apiUrl + "mr/internal-audit-report/")
        .then(function(response) {
          self.tlist = response.data;
        })
        .catch(function(error) {
          console.log(error.data);
        });
    },
    getAreaofAudit() {
      var self = this;
      axios
        .get(this.$apiUrl + "mr/internal-audit-plan/")
        .then(function(response) {
          self.areaOfAudit = response.data;
        })
        .catch(function(error) {
          console.log(error.data);
        });
    },
    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.tlist[this.editedIndex], this.editedItem);
      } else {
        var self = this;
        axios
          .post(this.$apiUrl + "mr/internal-audit-report/", {
            area_of_audit: this.tlist.area_of_audit,
            audit_check_point: this.tlist.audit_check_point,
            observations: this.tlist.observations,
            owner: this.$owner
          })
          .then(function(response) {
            self.getall();
          })
          .catch(function(error) {
            console.log(error);
          });
      }
      this.close();
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
            .delete(this.$apiUrl + "mr/internal-audit-report/" + did)
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
    close() {
      this.dialog = false;
      setTimeout(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      }, 300);
    },
    
  }
};
</script>
