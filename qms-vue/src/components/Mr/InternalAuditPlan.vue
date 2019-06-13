<template>
  <div>
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">Internal Audit Plan</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right">
          <v-dialog v-model="dialog" max-width="600px">
            <template v-slot:activator="{ on }">
              <v-btn-toggle class="transparent mr-2">
                  <v-btn flat  v-on="on" value="right">
                    <v-icon color="info">add</v-icon>
                    <span>Add New</span>
                  </v-btn>
              </v-btn-toggle>
            </template>
            <v-card>

              <v-card-text>
                <v-container grid-list-md>
                  <v-layout wrap>
                    <v-flex xs12 >
                      <span class="headline">{{ formTitle }} Internal Audit Plan</span>
                    </v-flex>
                    <v-flex xs12 sm6 md6>
                      <v-select v-model="tlist.year" :items="years" label="Year"></v-select>
                    </v-flex>
                    <v-flex xs12 sm6 md6>
                      <v-select
                        v-model="tlist.month"
                        :items="$month"
                        item-text="title"
                        item-value="value"
                        label="Month"
                      ></v-select>
                    </v-flex>
                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="tlist.area_of_audit" label="Area of Audit	"></v-text-field>
                    </v-flex>
                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="tlist.auditee" label="Auditee"></v-text-field>
                    </v-flex>
                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="tlist.auditor" label="Auditor"></v-text-field>
                    </v-flex>
                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="tlist.as_clauses" label="AS9100 Clauses"></v-text-field>
                    </v-flex>
                    <v-flex xs12 sm6 md6>
                      <v-select
                        v-model="tlist.status"
                        :items="status"
                        item-text="text"
                        item-value="value"
                        label="Status"
                      ></v-select>
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
        <td class="text-xs-left">{{ props.item.area_of_audit }}</td>
        <td class="text-xs-left">{{ props.item.auditee}}</td>
        <td class="text-xs-left">{{ props.item.auditor }}</td>
        <td class="text-xs-left">{{ props.item.as_clauses}}</td>
        <td class="text-xs-left">{{ props.item.year}}</td>
        <td class="text-xs-left">{{ props.item.month}}</td>
        <td class="text-xs-left">
          <v-icon small class="mr-3" color="info" @click="editItem(props.item)">edit</v-icon>
          <v-icon small color="red" @click="deleteData(props.item.id)">delete</v-icon>
        </td>
      </template>
    </v-data-table>

    <v-dialog v-model="editdialog" max-width="600px">

      <v-card>
        <v-card-text>
          <v-container grid-list-md>
            <v-layout wrap>
              <v-flex xs12 >
                <span class="headline">{{ formTitle }} Internal Audit Plan</span>
              </v-flex>
              <v-flex xs12 sm6 md6>
                <v-select v-model="editedItem.year" :items="years" label="Year"></v-select>
              </v-flex>

              <v-flex xs12 sm6 md6>
                <v-select
                        v-model="editedItem.month"
                        :items="$month"
                        item-text="title"
                        item-value="value"
                        label="Month"
                ></v-select>
              </v-flex>
              <v-flex xs12 sm6 md6>
                <v-text-field v-model="editedItem.area_of_audit" label="Area of Audit	"></v-text-field>
              </v-flex>
              <v-flex xs12 sm6 md6>
                <v-text-field v-model="editedItem.auditee" label="Auditee"></v-text-field>
              </v-flex>
              <v-flex xs12 sm6 md6>
                <v-text-field v-model="editedItem.auditor" label="Auditor"></v-text-field>
              </v-flex>
              <v-flex xs12 sm6 md6>
                <v-text-field v-model="editedItem.as_clauses" label="AS9100 Clauses"></v-text-field>
              </v-flex>
              <v-flex xs12 sm6 md6>
                <v-select
                        v-model="editedItem.status"
                        :items="status"
                        item-text="text"
                        item-value="value"
                        label="Status"
                ></v-select>
              </v-flex>
            </v-layout>
          </v-container>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" flat @click="editdialog = false">Cancel</v-btn>
          <v-btn color="blue darken-1" flat @click="save">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
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
        { text: "Area of Audit", value: "area_of_audit" },
        { text: "Auditee", value: "auditee" },
        { text: "Auditor", value: "auditor" },
        { text: "AS9100 Clauses", value: "as_clauses" },
        { text: "Year", value: "year" },
        { text: "Month", value: "month" },
        { text: "Action", value: "" }
      ],
      status: [{ value: "p", text: "Plan" }, { value: "c", text: "Completed" }],
      tlist: [],
      years: [],
      dialog: false,
      editdialog: false,
      editedIndex: -1,
      editedItem: {
        year: "",
        month: "",
        area_of_audit: "",
        auditee: "",
        auditor: "",
        as_clauses: "",
        status: "",
      }
    };
  },
  mounted() {
    this.getall();
    this.genYears();
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
        .get(this.$apiUrl + "mr/internal-audit-plan/")
        .then(function(response) {
          self.tlist = response.data;
        })
        .catch(function(error) {
          console.log(error.data);
        });
    },
    save() {
      if (this.editedIndex > -1) {
        // Object.assign(this.tlist[this.editedIndex], this.editedItem);
        var self = this;
        axios
                .put(this.$apiUrl + "mr/internal-audit-plan/" + this.editedItem.id + "/", {
                  area_of_audit: this.editedItem.area_of_audit,
                  auditee: this.editedItem.auditee,
                  auditor: this.editedItem.auditor,
                  as_clauses: this.editedItem.as_clauses,
                  year: this.editedItem.year,
                  month: this.editedItem.month,
                  status: this.editedItem.status,
                  owner: this.$owner
                })
                .then(function(response) {
                  self.getall();
                })
                .catch(function(error) {
                  console.log(error);
                });
          self.getall();
          this.editdialog = false;
      } else {
        var self = this;
        axios
          .post(this.$apiUrl + "mr/internal-audit-plan/", {
            area_of_audit: this.tlist.area_of_audit,
            auditee: this.tlist.auditee,
            auditor: this.tlist.auditor,
            as_clauses: this.tlist.as_clauses,
            year: this.tlist.year,
            month: this.tlist.month,
            status: this.tlist.status,
            owner: this.$owner
          })
          .then(function(response) {
            self.getall();
          })
          .catch(function(error) {
            console.log(error);
          });
        this.close();
      }

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
            .delete(this.$apiUrl + "mr/internal-audit-plan/" + did)
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
      this.editdialog = true;
      console.log(this.editedItem)
    },
    close() {
      this.dialog = false;
      setTimeout(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      }, 300);
    },
    genYears() {
      for (let index = new Date().getFullYear(); index < 2100; index++) {
        this.years.push(index);
      }
    }
  }
};
</script>
