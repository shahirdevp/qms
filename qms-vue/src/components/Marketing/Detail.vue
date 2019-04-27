<template>
  <div class>
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">Marketing</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right">
          <v-btn-toggle class="transparent">
            <router-link :to="{ path: '../marketing-enquiry-edit/' + detail.id }" replace>
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
    <v-layout>
      <v-flex xs12 sm12 md12>
        <v-layout row class="lay-des" wrap>
          <v-flex md3>
            <p>
              <strong>SINO :</strong>
              {{ detail.id }}
            </p>
          </v-flex>
          <v-flex md3>
            <p>
              <strong>Date :</strong>
              {{ detail.date }}
            </p>
          </v-flex>
          <v-flex md3>
            <p>
              <strong>Customer :</strong>
              {{ detail.customer }}
            </p>
          </v-flex>
          <v-flex md3>
            <p>
              <strong>Contact :</strong>
              {{ detail.contryCode +' '+ detail.contact }}
            </p>
          </v-flex>
        </v-layout>
        <v-layout row wrap>
          <v-flex md6>
            <div class="ees">
              <p>
                <strong>Line no :</strong>
                {{ detail.line_number }}
              </p>
              <p>
                <strong>Part Namber :</strong>
                {{ detail.partNumber }}
              </p>
              <p>
                <strong>Description :</strong>
                {{ detail.description }}
              </p>
              <p>
                <strong>Drawing Number :</strong>
                {{ detail.drawingNumber }}
              </p>
              <p>
                <strong>Qty :</strong>
                {{ detail.qty }}
              </p>
            </div>
          </v-flex>
          <v-flex md6>
            <div class="ees">
              <p>
                <strong>Quotation Ref :</strong>
                {{ detail.quotationRef }}
              </p>
              <p>
                <strong>Status :</strong>
                {{ detail.status }}
              </p>

              <p>
                <strong>PO .NO :</strong>
                {{ detail.poNumber }}
              </p>
            </div>
          </v-flex>
        </v-layout>
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
        .get(this.$apiUrl + "mkt/enquery-register/" + parQuery + '/')
        .then(function(response) {
          self.detail = response.data;
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
            .delete(this.$apiUrl + "mkt/enquery-register/" + parQuery + '/')
            .then(function(response) {
              swal({
                title: "Success",
                text: "Successfully Delete",
                type: "success",
                showConfirmButton: false,
                showCloseButton: false,
                timer: 3000
              });
              router.push("/marketing-enquiry");
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





