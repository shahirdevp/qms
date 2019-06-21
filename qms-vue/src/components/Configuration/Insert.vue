<template>
  <div id="empd">
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">Configuration Management</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right"></div>
      </v-flex>
    </v-layout>

    <!-- Insert-list-form -->
    <v-layout container>
      <v-flex xs12 sm12 md12>
        <v-card>
         
          <v-form ref="form" class="lay-des1 white" v-model="valid" id="emp" lazy-validation>
            <v-layout class="white" row wrap>
              
              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for black--text">Customer Order</label>
                  <v-text-field
                    v-model="detail.customer_order"
                    placeholder="Enter the value"
                    outline
                  ></v-text-field>
                </div>
              </v-flex>

              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for black--text">Date</label>
                  <v-dialog
                    ref="dialog"
                    v-model="detail.creadedOn"
                    :return-value.sync="date"
                    persistent
                    lazy
                    full-width
                    width="290px"
                  >
                    <template v-slot:activator="{ on }">
                      <v-text-field
                        v-model="date"
                        prepend-icon="event"
                        readonly
                        v-on="on"
                        label
                        placeholder=" Date"
                        outline
                      ></v-text-field>
                    </template>
                    <v-date-picker v-model="date" scrollable>
                      <v-spacer></v-spacer>
                      <v-btn flat color="primary" @click="modal = false">Cancel</v-btn>
                      <v-btn flat color="primary" @click="$refs.dialog.save(date)">OK</v-btn>
                    </v-date-picker>
                  </v-dialog>
                </div>
              </v-flex>

              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for black--text">Customer Name</label>
                  <v-text-field label v-model="detail.cusomer" placeholder="Customer Name" outline></v-text-field>
                </div>
              </v-flex>

               <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for black--text">Part No</label>
                  <v-text-field
                    label
                    v-model="detail.route_card_no"
                    placeholder="Route Card No"
                    outline
                  ></v-text-field>
                </div>
              </v-flex>

              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for black--text">Rev No</label>
                  <v-text-field
                    label
                    v-model="detail.route_card_no"
                    placeholder="Route Card No"
                    outline
                  ></v-text-field>
                </div>
              </v-flex>

              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for black--text">Drawing No</label>
                  <v-text-field
                    label
                    v-model="detail.route_card_no"
                    placeholder="Route Card No"
                    outline
                  ></v-text-field>
                </div>
              </v-flex>

              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for black--text">Drawing Rev No</label>
                  <v-text-field
                    label
                    v-model="detail.route_card_no"
                    placeholder="Route Card No"
                    outline
                  ></v-text-field>
                </div>
              </v-flex>

              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for black--text">Route Card No</label>
                  <v-text-field
                    label
                    v-model="detail.route_card_no"
                    placeholder="Route Card No"
                    outline
                  ></v-text-field>
                </div>
              </v-flex>

              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for black--text">Date</label>
                  <v-dialog
                    ref="dialog"
                    v-model="detail.creadedOn"
                    :return-value.sync="date"
                    persistent
                    lazy
                    full-width
                    width="290px"
                  >
                    <template v-slot:activator="{ on }">
                      <v-text-field
                        v-model="date"
                        prepend-icon="event"
                        readonly
                        v-on="on"
                        label
                        placeholder=" Date"
                        outline
                      ></v-text-field>
                    </template>
                    <v-date-picker v-model="date" scrollable>
                      <v-spacer></v-spacer>
                      <v-btn flat color="primary" @click="modal = false">Cancel</v-btn>
                      <v-btn flat color="primary" @click="$refs.dialog.save(date)">OK</v-btn>
                    </v-date-picker>
                  </v-dialog>
                </div>
              </v-flex>

              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for black--text">Internal Job Order</label>
                  <v-text-field
                    label
                    v-modal="detail.internal_job_order"
                    placeholder="Internal Job Order"
                    outline
                  ></v-text-field>
                </div>
              </v-flex>

              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for black--text">Date</label>
                  <v-dialog
                    ref="dialog"
                    v-model="detail.creadedOn"
                    :return-value.sync="date"
                    persistent
                    lazy
                    full-width
                    width="290px"
                  >
                    <template v-slot:activator="{ on }">
                      <v-text-field
                        v-model="date"
                        prepend-icon="event"
                        readonly
                        v-on="on"
                        label
                        placeholder=" Date"
                        outline
                      ></v-text-field>
                    </template>
                    <v-date-picker v-model="date" scrollable>
                      <v-spacer></v-spacer>
                      <v-btn flat color="primary" @click="modal = false">Cancel</v-btn>
                      <v-btn flat color="primary" @click="$refs.dialog.save(date)">OK</v-btn>
                    </v-date-picker>
                  </v-dialog>
                </div>
              </v-flex>

              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for black--text">Control Plan</label>
                  <v-text-field label v-model="detail.rev_no" placeholder="Rev No" outline></v-text-field>
                </div>
              </v-flex>

              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for black--text">Control Plan Rev No</label>
                  <v-text-field label v-model="detail.rev_no" placeholder="Rev No" outline></v-text-field>
                </div>
              </v-flex>

              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for black--text">Stage Drawing</label>
                  <v-text-field label v-model="detail.rev_no" placeholder="Rev No" outline></v-text-field>
                </div>
              </v-flex>

              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for black--text">Stage Drawing Rev No</label>
                  <v-text-field label v-model="detail.rev_no" placeholder="Rev No" outline></v-text-field>
                </div>
              </v-flex>

              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for black--text">Machine used</label>
                  <v-text-field label v-model="detail.rev_no" placeholder="Rev No" outline></v-text-field>
                </div>
              </v-flex>

              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for black--text">Operator</label>
                  <v-text-field label v-model="detail.rev_no" placeholder="Rev No" outline></v-text-field>
                </div>
              </v-flex>

              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for black--text">Tool List</label>
                  <v-text-field label v-model="detail.rev_no" placeholder="Rev No" outline></v-text-field>
                </div>
              </v-flex>

              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for black--text">Invoice No</label>
                  <v-text-field v-modal="detail.invoice_no" label placeholder="Invoice No" outline></v-text-field>
                </div>
              </v-flex>

              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for black--text">Invoice Date</label>
                  <v-dialog
                    ref="dialog"
                    v-model="detail.creadedOn"
                    :return-value.sync="date"
                    persistent
                    lazy
                    full-width
                    width="290px"
                  >
                    <template v-slot:activator="{ on }">
                      <v-text-field
                        v-model="date"
                        prepend-icon="event"
                        readonly
                        v-on="on"
                        label
                        placeholder=" Date"
                        outline
                      ></v-text-field>
                    </template>
                    <v-date-picker v-model="date" scrollable>
                      <v-spacer></v-spacer>
                      <v-btn flat color="primary" @click="modal = false">Cancel</v-btn>
                      <v-btn flat color="primary" @click="$refs.dialog.save(date)">OK</v-btn>
                    </v-date-picker>
                  </v-dialog>
                </div>
              </v-flex>

            </v-layout>


            <v-flex md12>
              <v-btn :disabled="!valid" color="success" @click="validate">Save</v-btn>
              <v-btn color="error" @click="reset">cancel</v-btn>
            </v-flex>


          </v-form>
        </v-card>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import swal from "sweetalert2";
import router from "../../router";

export default {
  data() {
    return {
      modal: false,
      // step-form
      e13: 2,
      detail: [],
      dn: true,
      date: "",
      //  push to database
      valid: true,
      // languages
      creadedOn: "",
      // form rules or validation
      positionRules: [v => !!v || "Employee Id is required"],
      eduBackgRules: [v => !!v || "Employee Id is required"],
      expRules: [v => !!v || "Employee Id is required"],
      competencyRules: [v => !!v || "Employee Id is required"],
      // department
      department: ["1", "2", "3", "4", "5"],
      // designation
      designation: ["D1", "D2", "D3", "D4", "D5"],
      // skills
      s1: ["Not Awarded", "Awarded", "Not In Scope", "Pending"],
      yn: ["Yes", "No"]
    };
  },
  methods: {
    validate() {
      if (this.$refs.form.validate()) {
        this.snackbar = true;
        console.log(this.detail);

        axios
          .post(this.$apiUrl + "mkt/configuration-management-report/", {
            cusomer: this.detail.cusomer,
            owner: this.detail.owner,
            customer_order: this.customer_order,
            route_card_no: this.detail.route_card_no,
            internal_job_order: this.detail.internal_job_order,
            rev_no: this.detail.rev_no,
            invoice_no: this.detail.invoice_no,
            creadedOn: this.detail.creadedOn,
            owner: this.$owner
          })
          .then(function(response) {
            console.log(response.data);

            // router.push("/configration-management/"+response.data.id);
          })
          .catch(function(error) {
            console.log(error);
          });
      }
    },
    reset() {
      this.$refs.form.reset();
    }
  }
};
</script>


<style scoped>
.two-column {
  column-count: 2;
  column-gap: 15px;
}
.three-column {
  column-count: 3;
  column-gap: 15px;
}
</style>
