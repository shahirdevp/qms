<template>
  <div>
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">Marketing Enquery Register</h3>
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
                      <span class="headline">Marketing Enquery Register</span>
                    </v-flex>
                    

                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="tlist.customer" label="Customer"></v-text-field>
                    </v-flex>

                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="tlist.date" label="Date" placeholder=" " type="Date"></v-text-field>
                    </v-flex>
                    
                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="tlist.contact" label="Contact" type="Number"></v-text-field>
                    </v-flex>

                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="tlist.line_number" label="Line Number" ></v-text-field>
                    </v-flex>

                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="tlist.partNumber" label="Part Number" ></v-text-field>
                    </v-flex>

                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="tlist.drawingNumber" label="Drawing Number" type="number"></v-text-field>
                    </v-flex>

                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="tlist.qty" label="QTY" type="number"></v-text-field>
                    </v-flex>

                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="tlist.quotationRef" label="Quotation Ref." ></v-text-field>
                    </v-flex>

                    <v-flex xs12 sm6 md6>
                      <v-select :items="status" item-text="title" item-value="title" v-model="tlist.status" label="Doc Status" ></v-select>
                    </v-flex>

                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="tlist.poNumber" label="PO Number" ></v-text-field>
                    </v-flex>

                    <v-flex xs12 >
                      <v-textarea v-model="tlist.description" label="Description" rows="2"></v-textarea>
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
        <td  class="text-xs-left">{{ props.item.id }}</td>
        <td class="text-xs-left">{{ props.item.date }}</td>
        <td class="text-xs-left">{{ props.item.customer }}</td>
        <td class="text-xs-left">{{ props.item.contact }}</td>
        <td class="text-xs-left">{{ props.item.line_number }}</td>
        <td class="text-xs-left">{{ props.item.partNumber }}</td>
        <td class="text-xs-left">{{ props.item.drawingNumber}}</td>
        <td class="text-xs-left">{{ props.item.qty }}</td>
        <!-- <td class="text-xs-left">{{ props.item.prodeliverDate}}</td> -->
        <td class="text-xs-left">{{ props.item.status}}</td>
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
                    <v-flex xs12>
                      <span class="headline">Edit  Marketing Enquery Register</span>
                    </v-flex>
                    

                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="editedItem.customer" label="Customer"></v-text-field>
                    </v-flex>

                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="editedItem.date" label="Date" placeholder=" " type="Date"></v-text-field>
                    </v-flex>
                    
                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="editedItem.contact" label="Contact" type="Number"></v-text-field>
                    </v-flex>

                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="editedItem.line_number" label="Line Number" ></v-text-field>
                    </v-flex>

                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="editedItem.partNumber" label="Part Number" ></v-text-field>
                    </v-flex>

                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="editedItem.drawingNumber" label="Drawing Number" type="number"></v-text-field>
                    </v-flex>

                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="editedItem.qty" label="QTY" type="number"></v-text-field>
                    </v-flex>

                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="editedItem.quotationRef" label="Quotation Ref." ></v-text-field>
                    </v-flex>

                    <v-flex xs12 sm6 md6>
                      <v-select :items="status" item-text="title" item-value="title" v-model="editedItem.status" label="Doc Status" ></v-select>
                    </v-flex>

                    <v-flex xs12 sm6 md6>
                      <v-text-field v-model="editedItem.poNumber" label="PO Number" ></v-text-field>
                    </v-flex>

                    <v-flex xs12 >
                      <v-textarea v-model="editedItem.description" label="Description" rows="2"></v-textarea>
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
        { text:"SL NO", value:'id' },
        { text: 'Date', value:'date' },
        { text: "Customer", value: "customer" },
        { text: "Contact", value: "contact" },
        { text: "Line No", value: "line_number" },
        { text: "Part Number", value: "partNumber" },
        { text: "Drawing Number", value: "drawingNumber" },
        { text: "Qty", value: "qty" },
        // { text: "Date", value: "prodeliverDate" },
        { text: "Status", value: "status" },
        { text: "Action", value: "" }
      ],
      select: null,
      options: [{ text: "AWARDED", value: "AWARDED" }, { text: "NOT AWARDED", value: "NOT AWARDED" }, { text: "PENDING", value: "PENDING" }, { text: "NOT IN SCOPE", value: "NOT IN SCOPE" },],
      tlist: [],
      doctype:[],
      dialog: false,
      editdialog: false,
      status:[ {title : 'Active'}, {title : 'Obsolete'}, ],
      type_of_doc:[ {title:"Internal document"}, {title:"External document"}, ],
      editedIndex: -1,
      editedItem: {
       id: '',
       customer: '',
       date: '',
       prodeliverDate: '',
       contact: '',
       contryCode: '',
       line_number: '',
       partNumber: '',
       description: '',
       drawingNumber: '',
       qty: '',
       quotationRef: '',
       status: '',
       poNumber: '',
       creadedOn: '',
       owner: '',
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
        .get(this.$apiUrl + "mkt/enquery-register/")
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
        
        var self = this;
        axios
         .put(this.$apiUrl + "mkt/enquery-register/" + this.editedItem.id + "/", {
            customer: this.editedItem.customer,
            date: this.editedItem.date,
            prodeliverDate: this.editedItem.prodeliverDate,
            contact: this.editedItem.contact,
            line_number: this.editedItem.line_number,
            partNumber: this.editedItem.partNumber,
            description: this.editedItem.description,
            drawingNumber: this.editedItem.drawingNumber,
            qty: this.editedItem.qty,
            quotationRef: this.editedItem.quotationRef,
            status: this.editedItem.status,
            poNumber: this.editedItem.poNumber,
            creadedOn: this.editedItem.creadedOn,
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
          .post(this.$apiUrl + "mkt/enquery-register/", {
            customer: this.tlist.customer,
            date: this.tlist.date,
            prodeliverDate: this.tlist.prodeliverDate,
            contact: this.tlist.contact,
            line_number: this.tlist.line_number,
            partNumber: this.tlist.partNumber,
            description: this.tlist.description,
            drawingNumber: this.tlist.drawingNumber,
            qty: this.tlist.qty,
            quotationRef: this.tlist.quotationRef,
            status: this.tlist.status,
            poNumber: this.tlist.poNumber,
            creadedOn: this.tlist.creadedOn,
           
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
            .delete(this.$apiUrl + "mkt/enquery-register/" + did)
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
