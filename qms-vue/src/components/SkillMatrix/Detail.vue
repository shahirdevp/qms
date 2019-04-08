<template>
    <div id="empd">
        <v-layout row wrap class="action-bar">
            <v-flex xs6>
                <h3 class="page-name">Skill Matrix Detail</h3>
            </v-flex>
            <v-flex xs6>
                <div class="text-xs-right">
                    <div :class="{dn : !dn}">
                            <v-tooltip v-model="show" bottom>
          <template v-slot:activator="{ on }">
            <v-btn icon v-on="on" ref="fileInput"  @click.stop="dn = !dn" >
             <v-icon  color="info">edit</v-icon>
            </v-btn>
          </template>
          <span>Edit</span>
        </v-tooltip>
         <v-tooltip v-model="show" bottom>
          <template v-slot:activator="{ on }">
            <v-btn icon v-on="on" ref="fileInput"  @click="deleteData()" >
             <v-icon  color="red">delete</v-icon>
            </v-btn>
          </template>
          <span>Delete</span>
        </v-tooltip>
                    </div>

                    <div :class="{dn : dn}">
                            <v-tooltip v-model="show" bottom>
          <template v-slot:activator="{ on }">
            <v-btn icon v-on="on" ref="fileInput" @click.stop="dn = !dn" >
             <v-icon  color="warning">close</v-icon>
            </v-btn>
          </template>
          <span>Cancel</span>
        </v-tooltip>
         <v-tooltip v-model="show" bottom>
          <template v-slot:activator="{ on }">
            <v-btn icon v-on="on" ref="fileInput" @click="validate()" >
             <v-icon  color="success">check</v-icon>
            </v-btn>
          </template>
          <span>Save</span>
        </v-tooltip>
                    </div>
                </div>
            </v-flex>
        </v-layout>

        <!-- Details-list -->
        <v-layout container>
            <v-flex xs12 sm12 md12>
                <v-card>
                    <v-layout class="lay-des" row wrap>
                        <v-flex md3 sm6>
                            <p><strong>Date : </strong> 05-04-2019</p>
                        </v-flex>
                        <v-flex md3 sm6>
                            <p><strong>Title : </strong> Testing</p>
                        </v-flex>
                        <v-flex md3 sm6>
                            <p><strong>Department : </strong> Ui Designer</p>
                        </v-flex>
                        <v-flex md3 sm6>
                            <p><strong>Designation : </strong> Front End Developer</p>
                        </v-flex>
                    </v-layout>
                    <div class="under-line"></div>
                    <!-- Dtails -->
                    <v-layout class="lay-des" row wrap>
                        <v-flex md6>
                            <p><strong>S No : </strong>001</p>
                            <p><strong>Name : </strong>Daniel Martin</p>
                            <p><strong>Employee ID : </strong>ID2091019</p>
                            <p><strong>Department : </strong> Ui Designer</p>
                            <p><strong>Designation : </strong> Front End Developer</p>
                        </v-flex>
                        <v-flex md6>
                            <p><strong>Scroing Crieteria</strong></p>
                            <ol class="list-scroing">
                                <li>Need Training</li>
                                <li>Can Work under supervision</li>
                                <li>Can Work alone</li>
                                <li>Can work & Train other</li>
                            </ol>
                        </v-flex>
                    </v-layout>
                    <div class="under-line"></div>
                    <v-layout class="lay-des" row wrap>
                        <v-flex xs12>
                            <p><strong>SKILLS</strong></p>
                        </v-flex>
                         <!--first list-->
                        <v-flex md6>
                            <v-layout row>
                                <v-flex md10>
                                    <p>Drawing studing skills </p>
                                    <p>Usage of general gauges </p>
                                    <p>Usage of general instruments</p>
                                    <p>Usage of product specific gauges</p>
                                    <p>Quality documentation</p>
                                    <p>CMM operating </p>
                                    <p>PP Operating </p>
                                </v-flex>
                                <v-flex md2>
                                    <p>4</p>
                                    <p>4</p>
                                    <p>6</p>
                                    <p>8</p>
                                    <p>8</p>
                                    <p>5</p>
                                    <p>9</p>
                                </v-flex>
                            </v-layout>
                        </v-flex>
                        <!--second list-->
                        <v-flex md6>
                            <v-layout row>
                                <v-flex md10>
                                    <p>Basic machining knowledge</p>
                                    <p>Internal verification skills</p>
                                    <p>Inspection skill</p>
                                    <p>Visual inspection skill</p>
                                    <p>2D height gauge operating</p>
                                    <p>Operating surface roughness tester</p>
                                    <p>Microscope Handeling</p>
                                </v-flex>
                                <v-flex md2>
                                    <p>4</p>
                                    <p>4</p>
                                    <p>6</p>
                                    <p>8</p>
                                    <p>8</p>
                                    <p>5</p>
                                    <p>9</p>
                                </v-flex>
                            </v-layout>
                        </v-flex>
                        <!--total value -->
                         <v-flex xs12>
                            <div class="total-value">
                            <p><strong>TOTAL : </strong> <span> 22 </span></p>
                            </div>
                        </v-flex>
                        <!-- end total value -->
                        <!--total value -->
                        <div class="under-line"></div>
                         <v-flex xs12 sm12 md12 >
                            <div class="ap-list">
                           <span class="ap-sp"> <p><strong>Powred By : </strong> <spam> Rishi Nath</spam></p></span>
                            <p><strong>Approved By : </strong> <spam> Shahir KM</spam></p>
                            </div>
                        </v-flex>
                        <!-- end total value -->
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

      // form rules or validation
      positionRules: [v => !!v || "Employee Id is required"],
      eduBackgRules: [v => !!v || "Employee Id is required"],
      expRules: [v => !!v || "Employee Id is required"],
      competencyRules: [v => !!v || "Employee Id is required"]
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
</style>

<style>
/*skill-matrix */
.lay-des {
    background: #fbfbfb;
    padding: 30px;
}
.skill-spac {
    line-height: 30px;
    padding: 0px;
        padding-left: 0px;
    padding-left: 15px;
}
.under-line {

    border-bottom: 1px dashed #bdbdbd;
    
    width: 100%;

}
.list-scroing {
    line-height: 30px;
    padding: 0px 0px 0px 14px;
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
::before, ::after {

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
  float: right;
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
@media (max-width: 768px){
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





