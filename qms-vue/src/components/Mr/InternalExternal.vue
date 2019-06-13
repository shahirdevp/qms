<template>
  <div>
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">Master list of Internal & External documents</h3>
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
                <v-container grid-list-md pd-0>
                  <v-layout wrap>
                    <v-flex xs12>
                      <span class="headline"> Internal & External Documents</span>
                    </v-flex>
                    <v-flex xs12 sm6 md6>
                      <v-select
                              v-model="tlist.type_of_doc"
                              :items="type_of_doc"
                              item-text="title"
                              item-value="title"
                              label="Select document for"
                      ></v-select>
                    </v-flex>

                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="tlist.doc_number" label="Document Number"></v-text-field>
                    </v-flex>

                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="tlist.doc_name" label="Document Name"></v-text-field>
                    </v-flex>
                    <v-flex xs12 sm6 md6>
                      <v-select
                        v-model="tlist.doc_type_name"
                        :items="doctype"
                        item-text="doc_type_name"
                        item-value="doc_type_name"
                        label="Type of Document"
                      ></v-select>
                    </v-flex>
                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="tlist.rev_no" label="Rev. No"></v-text-field>
                    </v-flex>
                    <v-flex xs12 sm6 md6>
                      <v-select :items="status" item-text="title" item-value="title" v-model="tlist.doc_status" label="Doc Status" ></v-select>
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
        <td class="text-xs-left">{{ props.item.type_of_doc }}</td>
        <td class="text-xs-left">{{ props.item.doc_number }}</td>
        <td class="text-xs-left">{{ props.item.doc_name }}</td>
        <td class="text-xs-left">{{ props.item.doc_type}}</td>
        <td class="text-xs-left">{{ props.item.rev_no }}</td>
        <td class="text-xs-left">{{ props.item.doc_status}}</td>
        <td class="text-xs-left">
          <v-icon small class="mr-3" color="info" @click="editItem(props.item)">edit</v-icon>
          <v-icon small color="red" @click="deleteData(props.item.id)">delete</v-icon>
        </td>
      </template>
    </v-data-table>

    <v-dialog v-model="editdialog" max-width="600px">
      <v-card>

        <v-card-text>
          <v-container grid-list-md pd-0>
            <v-layout wrap>
              <v-flex x12>
                <span class="headline">{{ formTitle }}Internal & External Document</span>
              </v-flex>
              <v-flex xs12 sm6 md6>
                <v-select
                        v-model="editedItem.type_of_doc"
                        :items="type_of_doc"
                        item-text="title"
                        item-value="title"
                        label="Select document for"
                ></v-select>
              </v-flex>
              <v-flex xs12 sm6 md6>
                <v-text-field v-model="editedItem.doc_number" label="Document Number"></v-text-field>
              </v-flex>
              <v-flex xs12 sm6 md6>
                <v-text-field v-model="editedItem.doc_name" label="Document Name"></v-text-field>
              </v-flex>
              <v-flex xs12 sm6 md6>
                <v-select
                        v-model="editedItem.doc_type_name"
                        :items="doctype"
                        item-text="doc_type_name"
                        item-value="doc_type_name"
                        label="Type of Document"
                ></v-select>
              </v-flex>
              <v-flex xs12 sm6 md6>
                <v-text-field v-model="editedItem.rev_no" label="Rev. No"></v-text-field>
              </v-flex>
              <v-flex xs12 sm6 md6>
                <v-select :items="status" item-text="title" item-value="title" v-model="editedItem.doc_status" label="Doc Status" ></v-select>
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
        { text: "Document For", value: "type_of_doc" },
        {
          text: "Document Number",
          align: "left",
          value: "doc_number"
        },
        { text: "Document Name", value: "doc_name" },
        { text: "Type of Document", value: "doc_type" },
        { text: "Rev. No.", value: "rev_no" },
        { text: "Doc Status", value: "doc_status" },
        { text: "Action", value: "" }
      ],
      select: null,
      options: [{ text: "Yes", value: "0" }, { text: "NO", value: "1" }],
      tlist: [],
      doctype:[],
      dialog: false,
      editdialog: false,
      status:[ {title : 'Active'}, {title : 'Obsolete'}, ],
      type_of_doc:[ {title:"Internal document"}, {title:"External document"}, ],
      editedIndex: -1,
      editedItem: {
        doc_number: "",
        doc_name: "",
        doc_type_name: "",
        rev_no: "",
        doc_status: "",
        type_of_doc:''
      }
    };
  },
  mounted() {
    this.getall();
    this.getType();
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
        .get(this.$apiUrl + "mr/internal-external-docs/")
        .then(function(response) {
          self.tlist = response.data;
        })
        .catch(function(error) {
          console.log(error.data);
        });
    },
    getType() {
      var self = this;
      axios
        .get(this.$apiUrl + "mr/doc-type/")
        .then(function(response) {
          self.doctype = response.data;
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
         .put(this.$apiUrl + "mr/internal-external-docs/" + this.editedItem.id + "/", {
           doc_number: this.editedItem.doc_number,
           doc_name: this.editedItem.doc_name,
           doc_type: this.editedItem.doc_type_name,
           rev_no: this.editedItem.rev_no,
           doc_status: this.editedItem.doc_status,
           type_of_doc: this.editedItem.type_of_doc
           //    owner : this.$owner,
         })
         .then(function(response) {
           self.getall();
         })
         .catch(function(error) {
           console.log(error);
         });
        this.editdialog = false;
      } else {
        var self = this;
        axios
          .post(this.$apiUrl + "mr/internal-external-docs/", {
            doc_number: this.tlist.doc_number,
            doc_name: this.tlist.doc_name,
            doc_type: this.tlist.doc_type_name,
            rev_no: this.tlist.rev_no,
            doc_status: this.tlist.doc_status,
            type_of_doc: this.tlist.type_of_doc
            //    owner : this.$owner,
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
            .delete(this.$apiUrl + "mr/internal-external-docs/" + did)
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
      setTimeout(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      }, 300);
    }
  }
};
</script>
