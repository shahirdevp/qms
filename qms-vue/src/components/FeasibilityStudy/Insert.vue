<template>
  <div id="empd">
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">Feasibility Study</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right">
          <div :class="{dn : !dn}">
            <v-tooltip v-model="show" bottom>
              <template v-slot:activator="{ on }">
                <v-btn icon v-on="on" ref="fileInput" @click.stop="dn = !dn">
                  <v-icon color="info">edit</v-icon>
                </v-btn>
              </template>
              <span>Edit</span>
            </v-tooltip>
            <v-tooltip v-model="show" bottom>
              <template v-slot:activator="{ on }">
                <v-btn icon v-on="on" ref="fileInput" @click="deleteData()">
                  <v-icon color="red">delete</v-icon>
                </v-btn>
              </template>
              <span>Delete</span>
            </v-tooltip>
          </div>

          <div :class="{dn : dn}">
            <v-tooltip v-model="show" bottom>
              <template v-slot:activator="{ on }">
                <v-btn icon v-on="on" ref="fileInput" @click.stop="dn = !dn">
                  <v-icon color="warning">close</v-icon>
                </v-btn>
              </template>
              <span>Cancel</span>
            </v-tooltip>
            <v-tooltip v-model="show" bottom>
              <template v-slot:activator="{ on }">
                <v-btn icon v-on="on" ref="fileInput" @click="validate()">
                  <v-icon color="success">check</v-icon>
                </v-btn>
              </template>
              <span>Save</span>
            </v-tooltip>
          </div>
        </div>
      </v-flex>
    </v-layout>

    <!-- Insert-list-form -->
    <v-layout container>
      <v-flex xs12 sm12 md12>
        <v-card>
          <v-layout class="lay-des-pad primary" row wrap>
            <v-flex xs12>
              <h3 class="head white--text">FEASIBILITY ENQUIRY FORM</h3>
            </v-flex>
          </v-layout>
          <v-stepper v-model="e13" vertical>
            <v-stepper-step step="1" complete>Name of step 1</v-stepper-step>
            <v-stepper-content step="1">
              <!-- <v-card color="grey lighten-1" class="mb-5" height="300px"> -->
              <v-layout class="white" row wrap>
                <v-flex md3>
                  <div class="text-rr">
                    <label class="lab-for grey--text">S.No</label>
                    <v-text-field placeholder="Enter your value" outline></v-text-field>
                  </div>
                </v-flex>
                <v-flex md3>
                  <div class="text-rr">
                    <label class="lab-for grey--text">Date</label>
                    <v-text-field placeholder="Enter your value" outline></v-text-field>
                  </div>
                </v-flex>
                <v-flex md3>
                  <div class="text-rr">
                    <label class="lab-for grey--text">Req No</label>
                    <v-text-field placeholder="Enter your value" outline></v-text-field>
                  </div>
                </v-flex>
                <v-flex md3>
                  <div class="text-rr">
                    <label class="lab-for grey--text">Line No</label>
                    <v-text-field placeholder="Enter your value" outline></v-text-field>
                  </div>
                </v-flex>
                <v-flex md3>
                  <div class="text-rr">
                    <label class="lab-for grey--text">Feasibility Stydy No</label>
                    <v-text-field placeholder="Enter your value" outline></v-text-field>
                  </div>
                </v-flex>
                <v-flex md3>
                  <div class="text-rr">
                    <label class="lab-for grey--text">Date</label>
                    <v-text-field placeholder="Enter your value" outline></v-text-field>
                  </div>
                </v-flex>
                <v-flex md3>
                  <div class="text-rr">
                    <label class="lab-for grey--text">Product Description</label>
                    <v-text-field placeholder="Enter your value" outline></v-text-field>
                  </div>
                </v-flex>
                <v-flex md3>
                  <div class="text-rr">
                    <label class="lab-for grey--text">Part Number</label>
                    <v-text-field placeholder="Enter your value" outline></v-text-field>
                  </div>
                </v-flex>
                <v-flex md3>
                  <div class="text-rr">
                    <label class="lab-for grey--text">Drawing Number</label>
                    <v-text-field placeholder="Enter your value" outline></v-text-field>
                  </div>
                </v-flex>
                <v-flex md3>
                  <div class="text-rr">
                    <label class="lab-for grey--text">Customer</label>
                    <v-text-field placeholder="Enter your value" outline></v-text-field>
                  </div>
                </v-flex>
                <v-flex md3>
                  <div class="text-rr">
                    <label class="lab-for grey--text">Qty</label>
                    <v-text-field placeholder="Enter your value" outline></v-text-field>
                  </div>
                </v-flex>
              </v-layout>
              <v-btn color="primary" @click="e13 = 2">Continue</v-btn>
              <v-btn flat>Cancel</v-btn>
            </v-stepper-content>

            <v-stepper-step step="2" complete>Name of step 2</v-stepper-step>

            <v-stepper-content step="2">
              <v-card color="grey lighten-1" class="mb-5" height="200px"></v-card>
              <v-btn color="primary" @click="e13 = 3">Continue</v-btn>
              <v-btn flat>Cancel</v-btn>
            </v-stepper-content>

            <v-stepper-step :rules="[() => false]" step="3">
              Ad templates
              <small>Alert message</small>
            </v-stepper-step>

            <v-stepper-content step="3">
              <v-card color="grey lighten-1" class="mb-5" height="200px"></v-card>
              <v-btn color="primary" @click="e13 = 4">Continue</v-btn>
              <v-btn flat>Cancel</v-btn>
            </v-stepper-content>

            <v-stepper-step step="4">View setup instructions</v-stepper-step>

            <v-stepper-content step="4">
              <v-card color="grey lighten-1" class="mb-5" height="200px"></v-card>
              <v-btn color="primary" @click="e13 = 1">Continue</v-btn>
              <v-btn flat>Cancel</v-btn>
            </v-stepper-content>
          </v-stepper>
          <v-form ref="form" v-model="valid" id="emp" lazy-validation>
            <!-- <div class="under-line"></div> -->
            <v-layout class="lay-des1 white" row wrap>
              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for grey--text">Customer Name</label>
                  <v-text-field placeholder="Customer Name" outline></v-text-field>
                </div>
              </v-flex>
              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for grey--text">Contact</label>
                  <v-text-field label placeholder="Contact" outline></v-text-field>
                </div>
              </v-flex>
              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for grey--text">Line No</label>
                  <v-text-field label placeholder="Line No" outline></v-text-field>
                </div>
              </v-flex>
              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for grey--text">Part Number</label>
                  <v-text-field label placeholder="Part Number" outline></v-text-field>
                </div>
              </v-flex>
              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for grey--text">Description</label>
                  <v-text-field label placeholder="Description" outline></v-text-field>
                </div>
              </v-flex>
              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for grey--text">Drawing Number</label>
                  <v-text-field label placeholder="Drawing Number" outline></v-text-field>
                </div>
              </v-flex>
              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for grey--text">Qty</label>
                  <v-text-field label placeholder="Qty" outline></v-text-field>
                </div>
              </v-flex>
              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for grey--text">Quotation Ref</label>
                  <v-text-field label placeholder="Quotation Ref" outline></v-text-field>
                </div>
              </v-flex>
              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for grey--text">Date</label>
                  <v-text-field label placeholder="Date" outline></v-text-field>
                </div>
              </v-flex>
              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for grey--text">Status</label>
                  <v-select class="field-sp" :items="s1" outline placeholder="Status"></v-select>
                </div>
              </v-flex>
              <v-flex md12>
                <v-btn :disabled="!valid" color="success" @click="validate">Save</v-btn>
                <v-btn color="error" @click="reset">cancel</v-btn>
              </v-flex>
            </v-layout>
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
      // step-form
      e13: 2,
      detail: [],
      dn: true,
      //  push to database
      valid: true,
      // languages
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
      s1: ["Not Awarded", "Awarded", "Not In Scope", "Pending"]
    };
  },
  mounted() {
    this.getdetails();
  },
  computed: {},
  methods: {
    getdetails() {
      var ts = window.location.pathname.split("/");
      var parQuery = ts[ts.length - 1];
      var self = this;
      axios
        .get("http://127.0.0.1:8000/api/v1/hr/completency/" + parQuery)
        .then(function(response) {
          self.detail = response.data;
        })
        .catch(function(error) {
          console.log(error.data);
        });
    },
    validate() {
      if (this.$refs.form.validate()) {
        this.snackbar = true;
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

<style>
/*skill-matrix */
.text-rr {
  margin: 5px;
}
.lab-for {
  font-weight: 600;
}
.text-rr input {
  margin-top: 10px;
  max-height: 21px;
}
.text-rr .v-input__slot {
  border: 1px solid rgba(0, 0, 0, 0.54) !important;
  min-height: 40px !important;
  margin: 5px 2px;
}
.text-rr .v-select__selections {
  padding-top: 0px !important;
}
.text-rr .v-input__append-inner {
  margin-top: 7px !important;
}
.under-line {
  border-bottom: 1px dashed #bdbdbd;
  width: 100%;
}
.radio-list .v-input {
  margin: 0px;
  padding-top: 7px;
}
.radio-list .v-icon {
  font-size: 14px;
}
.radio-list .v-lable {
  font-size: 14px;
}
.head {
  padding: 10px;
}
.lay-des1 {
  background: #fbfbfb;
  padding: 30px;
}
.lay-des-pad {
  padding: 10px 25px 5px;
}
.field-sp {
  padding: 10px;
}
.total-value p {
  float: right;
  margin-right: 52px;
  padding: 5px 25px;
  border-top: 1px solid;
  border-bottom: 1px solid;
}
.ap-list span {
  float: left;
  padding-right: 10px;
}
::before,
::after {
  text-decoration: inherit;
  vertical-align: inherit;
}
::selection {
  background-color: #b3d4fc;
  color: #000;
  text-shadow: none;
}
.ap-list {
  padding-top: 15px;
}
/* end skill-matrix */

.c-title {
  font-size: 20px;
  line-height: 35px;
  position: relative;
  margin-bottom: 20px;
}
.c-title:after {
  position: absolute;
  content: "";
  width: 100%;
  height: 1.5px;
  background-color: #e0e0e0;
  bottom: -5px;
  left: 0;
}
.c-list-lable {
  display: inline-block;
  width: 33%;
  color: #6f6f6f;
  padding: 0 5px 0 0px;
}
.c-list-content {
  display: inline-block;
  width: 67%;
  padding: 0 5px 0 0px;
}
.c-list {
  margin: 0 10px 25px 10px;
  padding: 10px 5px;
  width: calc(100% - 56px);
  position: relative;
}
.c-list::after {
  content: "";
  position: absolute;
  width: calc(100% - 65px);
  height: 1.5px;
  background: #dadada;
  left: 0;
  bottom: 0;
}
.c-list-lable::before {
  content: "";
  position: absolute;
  background: #77b8fb;
  height: 3px;
  width: 24%;
  bottom: -1px;
  left: 0px;
  z-index: 1;
}
.c-list-action {
  position: absolute;
  right: 4px;
  top: 0;
  width: 42px;
  opacity: 0;
  transition: 0.3s;
} /* .c-list:hover .c-list-action{opacity: 1;} */
.c-list-action .v-icon {
  font-size: 17px;
}
.c-right-date {
  display: inline-block;
  /* float: right; */
  position: absolute;
  right: 18px;
  top: 25px;
}
.dn {
  display: none;
}
.c-list-content-input input {
  width: calc(100% - 60px);
  border-bottom: 1px solid #fff0;
}
.c-list-content-input input:focus {
  border-bottom: 1px solid #77b8fb;
  box-shadow: 0px 5px 5px -7px #0042ff;
}
.block {
  display: block;
  width: 100%;
}
.form-box {
  width: calc(100% -65px);
  width: 90%;
} /*  input  */
.ic-list input,
.ic-list textarea,
.ic-list select {
  border: 1px solid #c6c6c6;
  width: calc(100% - 105px);
  padding: 8px 5px;
  margin-bottom: 15px;
  border-radius: 3px;
  margin-top: 3px;
}
.ic-list input:focus,
.ic-list textarea:focus,
.ic-list select:focus {
  border-color: #799df5;
  box-shadow: 0px 0px 3px #799df5;
}
.ic-list-lable {
  color: rgba(114, 114, 114, 1);
}
#empd .v-input__prepend-outer {
  display: none !important;
}
/* responsive */
@media (max-width: 768px) {
  .total-value p {
    float: right;
    margin-right: 0px;
  }
  .ap-list span {
    float: unset;
    padding-right: 0px;
    padding: 5px 10px;
  }
}
</style>





