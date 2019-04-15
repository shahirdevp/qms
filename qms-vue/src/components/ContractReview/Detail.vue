<template>
  <div class>
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">Order / Contract Review Report</h3>
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
    <!-- detail -->
    <v-layout container>
      <v-flex xs12 sm12 md12>
        <v-card>
          <v-layout class="lay-des-pad grey lighten-3" row wrap>
            <v-flex xs12>
              <h3 class="head black--text">CONTRACT REVIEW REPORT</h3>
            </v-flex>
          </v-layout>
          <!-- <div class="under-line"></div> -->
          <!-- first list -->
          <v-layout class="lay-des1 white" row wrap>
            <v-flex md6 xs12 sm6>
              <p>
                <strong>SINO :</strong> 1
              </p>
              <p>
                <strong>Date :</strong> 2-4-2019
              </p>
              <p>
                <strong>Customer / Contract :</strong> Text Dummy
              </p>
              <p>
                <strong>Part Number :</strong> 56
              </p>
              <p>
                <strong>Drawing Number :</strong> 3421
              </p>
            </v-flex>
            <v-flex md6 xs12 sm6>
              <p>
                <strong>Qty :</strong> 09809
              </p>
              <p>
                <strong>Description :</strong> The text dummy content
              </p>
              <p>
                <strong>Description :</strong> The text dummy content
              </p>
              <p>
                <strong>Agreed Delevery Date :</strong> 21-04-2019
              </p>
            </v-flex>
          </v-layout>
          <div class="under-line"></div>
          <!-- second-list -->
          <v-layout class="lay-des1 white" row wrap>
            <v-flex xs12>
              <h3 class>Production Feasibility :</h3>
              <br>
            </v-flex>
            <v-flex md3 xs12 sm6>
              <p>
                <strong>R/Mtrl :</strong> Yes
              </p>
            </v-flex>
            <v-flex md3 xs12 sm6>
              <p>
                <strong>M/c :</strong> No
              </p>
            </v-flex>
            <v-flex md3 xs12 sm6>
              <p>
                <strong>Tools :</strong> Yes
              </p>
            </v-flex>
            <v-flex md3 xs12 sm6>
              <p>
                <strong>Spl.Process :</strong> No
              </p>
            </v-flex>
            <v-flex md3 xs12 sm6>
              <p>
                <strong>Any CAD req :</strong> Yes
              </p>
            </v-flex>
            <v-flex md3 xs12 sm6>
              <p>
                <strong>Out source :</strong> Yes
              </p>
            </v-flex>
            <v-flex md3 xs12 sm6>
              <p>
                <strong>Suitable man power :</strong> Yes
              </p>
            </v-flex>
            <v-flex md3 xs12 sm6>
              <p>
                <strong>Risk involved :</strong> Yes
              </p>
            </v-flex>
          </v-layout>
          <div class="under-line"></div>
          <!-- third-list -->
          <v-layout class="lay-des1 white" row wrap>
            <v-flex xs12>
              <h3 class>Quality Feasibility :</h3>
              <br>
            </v-flex>
            <v-flex md3 xs12 sm6>
              <p>
                <strong>Inst :</strong> Yes
              </p>
            </v-flex>
            <v-flex md3 xs12 sm6>
              <p>
                <strong>Gauge :</strong> No
              </p>
            </v-flex>
            <v-flex md3 xs12 sm6>
              <p>
                <strong>Is FAI required :</strong> Yes
              </p>
            </v-flex>
            <v-flex md3 xs12 sm6>
              <p>
                <strong>Key chare :</strong> No
              </p>
            </v-flex>
            <v-flex md3 xs12 sm6>
              <p>
                <strong>Can AQL be achived :</strong> Yes
              </p>
            </v-flex>
            <v-flex md3 xs12 sm6>
              <p>
                <strong>Ispection as per :</strong> Yes
              </p>
            </v-flex>
          </v-layout>
          <div class="under-line"></div>
          <!-- four-list -->
          <v-layout class="lay-des1 white" row wrap>
            <v-flex xs12>
              <h3 class>Marketing Feasibility :</h3>
              <br>
            </v-flex>
            <v-flex md3 xs12 sm6>
              <p>
                <strong>Statuatory & Regulatory Req :</strong> Yes
              </p>
            </v-flex>
            <v-flex md3 xs12 sm6>
              <p>
                <strong>Delivery Feasibility :</strong> No
              </p>
            </v-flex>
            <v-flex md3 xs12 sm6>
              <p>
                <strong>Is NRE applicable :</strong> Yes
              </p>
            </v-flex>
          </v-layout>
          <div class="under-line"></div>
          <!-- five-list -->
          <v-layout class="lay-des1 white" row wrap>
            <v-flex xs12>
              <h3 class>Reviewer :</h3>
              <br>
            </v-flex>
            <v-flex md3 xs12 sm6>
              <p>
                <strong>Mkt :</strong> Yes
              </p>
            </v-flex>
            <v-flex md3 xs12 sm6>
              <p>
                <strong>QCD:</strong> No
              </p>
            </v-flex>
            <v-flex md3 xs12 sm6>
              <p>
                <strong>PUR:</strong> Yes
              </p>
            </v-flex>
            <v-flex md3 xs12 sm6>
              <p>
                <strong>PRD:</strong> Yes
              </p>
            </v-flex>
          </v-layout>
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
      detail: [],
      dn: true,
      //  push to database
      valid: true,
      // languages

      show1: false,
      detail: [],
      todos: [{ title: "todo one" }, { title: "todo two" }],
      todo: "",
      seen: false,
      hide: true
    };
  },
  mounted() {},
  computed: {},
  methods: {
    savetodolist() {
      this.todos.push({ title: this.todo });
      this.todo = "";
    },

    deleteEvent(index) {
      this.todos.splice(index, 1);
    },

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
    validate: function() {
      if (this.$refs.form.validate()) {
        this.snackbar = true;
        var self = this;

        var ts = window.location.pathname.split("/");
        var parQuery = ts[ts.length - 1];
        var self = this;

        axios({
          method: "put",
          url: "http://127.0.0.1:8000/api/v1/hr/completency/" + parQuery,
          data: {
            position: self.detail.position,
            education_Background: self.detail.education_Background,
            experience: self.detail.experience,
            competency_Requirement: self.detail.competency_Requirement
          }
        })
          .then(function(response) {
            self.dn = !response.dn;
            swal({
              title: "Success",
              type: "success",
              text: "Successfully edited",
              showConfirmButton: false,
              showCloseButton: false,
              timer: 3000
            });
          })
          .catch(function(error) {
            console.log(error);
          });
      }
    },
    deleteData() {
      var ts = window.location.pathname.split("/");
      var parQuery = ts[ts.length - 1];
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
            .delete("http://127.0.0.1:8000/api/v1/hr/completency/" + parQuery)
            .then(function(response) {
              swal({
                title: "Success",
                text: "Successfully Delete",
                type: "success",
                showConfirmButton: false,
                showCloseButton: false,
                timer: 3000
              });
              router.push("/compentency-matrix");
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
/*skill-matrix */
.lay-des {
  background: #fbfbfb;
  padding: 20px 25px 0px 25px;
  border-bottom: 1px dashed gray;
}
.lay-out-res {
  background: #1976d2;
  padding: 25px;
}
.bt-l {
  margin: 0px 10px;
}

.ap-list span {
  float: left;
  padding-right: 10px;
}
.lay-back {
  width: 100%;
  padding: 0px;
  margin: 0px;
  display: inline-flex;
}

/* end skill-matrix */
</style>

<style>
.v-list--two-line .v-list__tile {
  height: 50px !important;
}
.ee {
  background: #f3f3f3;
  padding: 25px;
}
.ees {
  padding: 20px 25px;
}

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





