<template>
  <div>
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">Approved Supplier</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right">
          <v-dialog v-model="dialog" max-width="500px">
            <template v-slot:activator="{ on }">
              <v-btn-toggle class="transparent mr-2">
                <v-btn flat v-on="on" value="right">
                  <v-icon color="info">add</v-icon>
                  <span>Add New</span>
                </v-btn>
              </v-btn-toggle>
            </template>
            <v-card>
              <v-card-title>
                <span class="headline">{{ formTitle }} Approved Supplier</span>
              </v-card-title>

              <v-card-text>
                <v-container grid-list-md>
                  <v-layout wrap>
                    <v-flex xs12 md12>
                      <v-select
                        v-model="tlist.supplier"
                        :items="supplier"
                        item-text="supplier"
                        item-value="id"
                        label="Supplier"
                      ></v-select>
                    </v-flex>
                    <v-flex xs12 md12>
                      <v-text-field v-model="tlist.scope" label="Scope"></v-text-field>
                    </v-flex>
                    <v-flex xs12>
                      <v-select
                        v-model="tlist.status"
                        :items="status"
                        item-text="value"
                        item-value="value"
                        label="Status"
                      ></v-select>
                    </v-flex>
                    <v-flex xs12>
                      <v-text-field type="date" v-model="tlist.next_approved_date" label="Next approved date "></v-text-field>
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
        <td class="text-xs-left">{{ props.item.supplier }}</td>
        <td class="text-xs-left">{{ props.item.scope}}</td>
        <td class="text-xs-left">{{ props.item.status }}</td>
        <td class="text-xs-left">{{ props.item.next_approved_date}}</td>
        <td class="text-xs-left">
          <v-icon small class="mr-3" color="info" @click="editItem(props.item)">edit</v-icon>
          <v-icon small color="red" @click="deleteData(props.item.id)">delete</v-icon>
        </td>
      </template>
    </v-data-table>

    <v-dialog v-model="editdialog" max-width="500px">
      <v-card>
        <v-card-title>
          <span class="headline">{{ formTitle }} Approved Supplier</span>
        </v-card-title>

        <v-card-text>
          <v-container grid-list-md>
            <v-layout wrap>
              <v-flex xs12 md12>
                <v-select
                  v-model="editedItem.supplier"
                  :items="supplier"
                  item-text="supplier"
                  item-value="id"
                  label="Supplier"
                ></v-select>
              </v-flex>
              <v-flex xs12 md12>
                <v-text-field v-model="editedItem.scope" label="Scope"></v-text-field>
              </v-flex>
              <v-flex xs12>
                <v-select
                  v-model="editedItem.status"
                  :items="status"
                  item-text="value"
                  item-value="value"
                  label="Status"
                ></v-select>
              </v-flex>
              <v-flex xs12>
                <v-text-field v-model="editedItem.next_approved_date" label="Next approved date "></v-text-field>
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
</template>

<script>
import axios from "axios";
import swal from "sweetalert2";
import router from "../../router";

export default {
  data() {
    return {
      headers: [
        { text: "SL NO ", align: "left", value: "id" },
        { text: "Supplier", value: "supplier" },
        { text: "Scope", value: "scope" },
        { text: "Status", value: "status" },
        { text: "Next approved date ", value: "next_approved_date" },
        { text: "Action", value: "" }
      ],
      status: [
        { value: "Approved" },
        { value: "Under Evaluation" },
        { value: "Restricted" },
        { value: "Disapproved" }
      ],
      tlist: [],
      editdialog:false,
      supplier: [],
      dialog: false,
      editedIndex: -1,
      editedItem: {
        id: "",
        supplier: "",
        scope: "",
        status: "",
        next_approved_date: ""
      }
    };
  },
  mounted() {
    this.getall();
    this.getSupplier();
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
        .get(this.$apiUrl + "pur/purchase-approved-supplier/")
        .then(function(response) {
          self.tlist = response.data;
        })
        .catch(function(error) {
          console.log(error.data);
        });
    },
    getSupplier() {
      var self = this;
      axios
        .get(this.$apiUrl + "pur/supplier/")
        .then(function(response) {
          self.supplier = response.data;
        })
        .catch(function(error) {
          console.log(error.data);
        });
    },
    save() {
      if (this.editedIndex > -1) {
        var self = this;
        axios
          .put(this.$apiUrl + "pur/purchase-approved-supplier/" + this.editedItem.id + "/", {
            supplier: this.editedItem.supplier,
            scope: this.editedItem.scope,
            status: this.editedItem.status,
            next_approved_date: this.editedItem.next_approved_date,
            owner: this.$owner
          })
          .then(function(response) {
             swal({
                title: "Success",
                text: "Successfully Updated",
                type: "success",
                showConfirmButton: false,
                showCloseButton: false,
                timer: 3000
              });
            self.getall();
          })
          .catch(function(error) {
            console.log(error);
          });
      } else {
        var self = this;
        axios
          .post(this.$apiUrl + "pur/purchase-approved-supplier/", {
            supplier: this.tlist.supplier,
            scope: this.tlist.scope,
            status: this.tlist.status,
            next_approved_date: this.tlist.next_approved_date,
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
            .delete(this.$apiUrl + "pur/purchase-approved-supplier/" + did)
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
    },
    close() {
      this.dialog = false;
      this.editdialog = false;
      setTimeout(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      }, 300);
    }
  }
};
</script>
