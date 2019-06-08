<template>
  <div>
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">HR REQUIRMENT REGISTER</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right">
          <div :class="{dn : !dn}">
            <v-btn color="info" ref="fileInput" @click.stop="dn = !dn">
              Edit
              <v-icon right>edit</v-icon>
            </v-btn>
            <v-btn color="red" dark ref="fileInput" @click="deleteData()">
              Delete
              <v-icon right>delete</v-icon>
            </v-btn>
          </div>

          <div :class="{dn : dn}">
            <v-btn color="warning" ref="fileInput" @click.stop="dn = !dn">
              Cancel
              <v-icon right>close</v-icon>
            </v-btn>

            <v-btn color="success" ref="fileInput" @click="postData()">
              Save
              <v-icon right>check</v-icon>
            </v-btn>
          </div>
        </div>
      </v-flex>
    </v-layout>

    <!-- Details -->
    <v-card style="margin:15px;padding:15px" :class="{ dn: !dn }">
      <v-layout row wrap>
        <v-flex xs12>
          <div class="c-title">{{ detail.hr_required_deg }}</div>
          <div class="c-right-date">HR/F/01 Rev: 00 Date: {{ detail.createdOn }}</div>
        </v-flex>
        <v-layout class="text-content" row wrap>
          <v-flex xs6>
            <div class="c-ul">
              <div class="c-list">
                <div class="c-list-lable">Sl No.</div>
                <div class="c-list-content">{{ detail.id }}</div>
                <div class="c-list-action text-xs-center">
                  <v-btn flat icon color="primary" small>
                    <v-icon>edit</v-icon>
                  </v-btn>
                </div>
              </div>

              <div class="c-list">
                <div class="c-list-lable">HR Required for Designation</div>
                <div class="c-list-content">{{ detail.hr_required_deg }}</div>
                <div class="c-list-action text-xs-center">
                  <v-btn flat icon color="primary" small>
                    <v-icon>edit</v-icon>
                  </v-btn>
                </div>
              </div>

              <div class="c-list">
                <div class="c-list-lable">No. Of HR</div>
                <div class="c-list-content">Need to check client</div>
                <div class="c-list-action text-xs-center">
                  <v-btn flat icon color="primary" small>
                    <v-icon>edit</v-icon>
                  </v-btn>
                </div>
              </div>

              <div class="c-list">
                <div class="c-list-lable">Reason for New Hiring</div>
                <div class="c-list-content">{{ detail.reson_new_hire }}</div>
                <div class="c-list-action text-xs-center">
                  <v-btn flat icon color="primary" small>
                    <v-icon>edit</v-icon>
                  </v-btn>
                </div>
              </div>
            </div>
          </v-flex>

          <v-flex xs6>
            <div class="c-ul">
              <div class="c-list">
                <div class="c-list-lable">Requestedby</div>
                <div class="c-list-content">{{ detail.requestedby }}</div>
                <div class="c-list-action text-xs-center">
                  <v-btn flat icon color="primary" small>
                    <v-icon>edit</v-icon>
                  </v-btn>
                </div>
              </div>

              <div class="c-list">
                <div class="c-list-lable">Remarks</div>
                <div class="c-list-content">{{ detail.remarks }}</div>
                <div class="c-list-action text-xs-center">
                  <v-btn flat icon color="primary" small>
                    <v-icon>edit</v-icon>
                  </v-btn>
                </div>
              </div>

              <div class="c-list">
                <div class="c-list-lable">PREPARED BY</div>
                <div class="c-list-content">{{ detail.preparedBy }}</div>
                <div class="c-list-action text-xs-center">
                  <v-btn flat icon color="primary" small>
                    <v-icon>edit</v-icon>
                  </v-btn>
                </div>
              </div>

              <div class="c-list">
                <div class="c-list-lable">APPROVED BY:</div>
                <div class="c-list-content">
                  <div class="c-list-content-con">{{ detail.arrovedBy }}</div>
                  <div class="c-list-content-input">
                    <input type="text" value="admin">
                  </div>
                </div>
                <div class="c-list-action text-xs-center">
                  <v-btn flat icon color="primary" small>
                    <v-icon>edit</v-icon>
                  </v-btn>
                </div>
              </div>
            </div>
          </v-flex>
        </v-layout>
      </v-layout>
    </v-card>

    <!-- Details -->
    <v-card style="margin:15px;padding:15px" :class="{ dn: dn }">
      <v-layout row wrap>
        <v-flex xs12>
          <div class="c-title">{{ detail.hr_required_deg }}</div>
          <div class="c-right-date">HR/F/01 Rev: 00 Date: {{ detail.createdOn }}</div>
        </v-flex>
        <v-form class="block" ref="form">
          <v-layout class="text-content" row wrap>
            <v-flex xs6>
              <div class="ic-ul">
                <div class="ic-list">
                  <div class="ic-list-lable">Sl No.</div>
                  <input type="text" v-model="detail.id" readonly>
                </div>

                <div class="ic-list">
                  <div class="ic-list-lable">HR Required for Designation</div>
                  <input type="text" v-model="detail.hr_required_deg">
                </div>

                <div class="ic-list">
                  <div class="ic-list-lable">No. Of HR</div>
                  <input type="text" v-model="detail.hr_required_deg">
                </div>

                <div class="ic-list">
                  <div class="ic-list-lable">Reason for New Hiring</div>
                  <input type="text" v-model="detail.reson_new_hire">
                </div>
              </div>
            </v-flex>

            <v-flex xs6>
              <div class="ic-ul">
                <div class="ic-list">
                  <div class="ic-list-lable">Requestedby</div>
                  <input type="text" v-model="detail.requestedby">
                </div>

                <div class="ic-list">
                  <div class="ic-list-lable">Remarks</div>
                  <input type="text" v-model="detail.remarks">
                </div>

                <div class="ic-list">
                  <div class="ic-list-lable">PREPARED BY</div>
                  <input type="text" v-model="detail.preparedBy">
                </div>

                <div class="ic-list">
                  <div class="ic-list-lable">APPROVED BY:</div>
                  <div class="ic-list-content">
                    <input type="text" v-model="detail.arrovedBy">
                  </div>
                </div>
              </div>
            </v-flex>
          </v-layout>
        </v-form>
      </v-layout>
    </v-card>
  </div>
</template>

<style scoped>
.two-column {
  column-count: 2;
  column-gap: 15px;
}
</style>

<style>
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
}
/* .c-list:hover .c-list-action{opacity: 1;} */
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

/*  input  */
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
</style>



<script>
import swal from "sweetalert2";
import router from "../../router";

export default {
  data() {
    return {
      detail: [],
      dn: true
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
        .get(this.$apiUrl+"hr/" + parQuery)
        .then(function(response) {
          self.detail = response.data;
        })
        .catch(function(error) {
          console.log(error.data);
        });
    },
    postData() {
      var ts = window.location.pathname.split("/");
      var parQuery = ts[ts.length - 1];
      var self = this;
      axios({
        method: "put",
        url: this.$apiUrl+"hr/" + parQuery + "/",
        data: {
          arrovedBy: this.detail.arrovedBy,
          hr_required_deg: this.detail.hr_required_deg,
          preparedBy: this.detail.preparedBy,
          remarks: this.detail.remarks,
          requestedby: this.detail.requestedby,
          reson_new_hire: this.detail.reson_new_hire
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
          console.log(error.data);
        });
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
            .delete(this.$apiUrl+"hr/" + parQuery + "/")
            .then(function(response) {
              swal({
                title: "Success",
                text: "Successfully Delete",
                type: "success",
                showConfirmButton: false,
                showCloseButton: false,
                timer: 3000
              });
              router.push("/hr-list");
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

