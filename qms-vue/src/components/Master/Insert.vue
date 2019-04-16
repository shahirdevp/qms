<template>
  <div id="empd">
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">Master List Of Internal & External Document</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right">
          <div :class="{dn : !dn}">
            <v-tooltip bottom>
              <template v-slot:activator="{ on }">
                <v-btn icon v-on="on" ref="fileInput" @click.stop="dn = !dn">
                  <v-icon color="info">edit</v-icon>
                </v-btn>
              </template>
              <span>Edit</span>
            </v-tooltip>
            <v-tooltip bottom>
              <template v-slot:activator="{ on }">
                <v-btn icon v-on="on" ref="fileInput" @click="deleteData()">
                  <v-icon color="red">delete</v-icon>
                </v-btn>
              </template>
              <span>Delete</span>
            </v-tooltip>
          </div>

          <div :class="{dn : dn}">
            <v-tooltip bottom>
              <template v-slot:activator="{ on }">
                <v-btn icon v-on="on" ref="fileInput" @click.stop="dn = !dn">
                  <v-icon color="warning">close</v-icon>
                </v-btn>
              </template>
              <span>Cancel</span>
            </v-tooltip>
            <v-tooltip bottom>
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
          <v-layout class="lay-des-pad grey lighten-3" row wrap>
            <v-flex xs12>
              <h3 class="head black--text">Master List Of Internal & External Document</h3>
            </v-flex>
          </v-layout>
          <v-form ref="form" class="lay-des1 white" v-model="valid" id="emp" lazy-validation>
            <!-- <div class="under-line"></div> -->
            <v-layout class="white" row wrap>
              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for black--text">Document Number</label>
                  <v-text-field placeholder="Enter the value" outline></v-text-field>
                </div>
              </v-flex>
              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for black--text">Date</label>
                  <v-dialog
                    ref="dialog"
                    v-model="modal"
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
                  <label class="lab-for black--text">Rev No</label>
                  <v-text-field label placeholder="Rev No" outline></v-text-field>
                </div>
              </v-flex>
              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for black--text">Document Name</label>
                  <v-text-field label placeholder="Customer Name" outline></v-text-field>
                </div>
              </v-flex>
              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for black--text">Type of Document</label>
                  <v-text-field label placeholder="Type of Document" outline></v-text-field>
                </div>
              </v-flex>
              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for black--text">Document Satus</label>
                  <v-text-field label placeholder="Document Satus" outline></v-text-field>
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
      s1: ["Not Awarded", "Awarded", "Not In Scope", "Pending"],
      yn: ["Yes", "No"]
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
.pad20 {
  padding-bottom: 20px;
}
.text-rr {
  margin: 5px;
}
.lab-for {
  font-weight: 400;
}
.text-rr input {
  margin-top: 6px;
  max-height: 20px;
  font-size: 14px;
}
.text-rr .v-input__slot {
  border: 1px solid rgba(180, 180, 180, 0.54) !important;

  min-height: 35px !important;
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





