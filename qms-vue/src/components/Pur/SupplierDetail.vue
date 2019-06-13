<template>
  <div class>
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">Supplier</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right">
          <v-btn-toggle class="transparent">
            <router-link :to="{ path: '../suppliers-edit/' + detail.id }" replace>
              <v-btn flat value="left">
                <span>Edit</span>
                <v-icon color="info">edit</v-icon>
              </v-btn>
            </router-link>
            <v-btn @click="deleteData()" flat value="center">
              <span>Delete</span>
              <v-icon color="red">delete</v-icon>
            </v-btn>
          </v-btn-toggle>
        </div>
      </v-flex>
    </v-layout>
    <!-- detail -->


      <div class="card-box">
          <h4 class="card-box-title">Supplier Detail</h4>
          <table class="cards-table">
              <tr>
                  <th>Supplier</th>
                  <td>{{ detail.supplier }}</td>
              </tr>
              <tr>
                  <th>Phone</th>
                  <td>
                      <a :href="'tel:' + detail.phone">{{ detail.phone }}</a>
                  </td>
              </tr>
              <tr>
                  <th>Email</th>
                  <td><a :href="'mailto:'+  detail.email"  >{{ detail.email }}</a></td>
              </tr>
              <tr>
                  <th>Website</th>
                  <td><a target="_blank"  :href="detail.website" >{{ detail.website }}</a></td>
              </tr>
              <tr>
                  <th>Country</th>
                  <td>{{ detail.country }}</td>
              </tr>
              <tr>
                  <th>State</th>
                  <td>{{ detail.state }}</td>
              </tr>

              <tr>
                  <th>City</th>
                  <td>{{ detail.city }}</td>
              </tr>

              <tr>
                  <th>Street</th>
                  <td>{{ detail.street }}</td>
              </tr>

              <tr>
                  <th>Pin</th>
                  <td>{{ detail.pin }}</td>
              </tr>
          </table>
      </div>
  </div>
</template>

<script>
import swal from "sweetalert2";
import router from "../../router";

export default {
  data() {
    return {
      detail: []
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
        .get(this.$apiUrl + "pur/supplier/" + parQuery + '/')
        .then(function(response) {
          self.detail = response.data;
          console.log(response.data)
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
            .delete(this.$apiUrl + "pur/supplier/" + parQuery + '/')
            .then(function(response) {
              swal({
                title: "Success",
                text: "Successfully Delete",
                type: "success",
                showConfirmButton: false,
                showCloseButton: false,
                timer: 3000
              });
              router.push("/suppliers");
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
.custom-card-list div { padding: 4px 0; }
.custom-card-list .v-card__text{ padding: 15px; }
.custom-card-list h3 { font-size: 16px; font-weight: 400; color:rgba(0,0,0,0.87); line-height: 24px}

</style>





