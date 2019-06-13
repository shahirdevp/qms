<template>
  <div id="empd">
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">IA Nonconformance Report Create</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right"></div>
      </v-flex>
    </v-layout>

    <!-- Insert-list-form -->
    <v-layout row class="lay-des1 white">
      <v-flex xs12 sm12 md11>
        <v-form ref="form" class v-model="valid" id="emp" lazy-validation>
          <v-layout class="white" row wrap>
            <v-flex md2>
              <label class="lab-for right black--text">Area of audit</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-select
                        v-model="detail.area_of_audit"
                        :items="auditArea"
                        item-text="area_of_audit"
                        item-value="id"
                        label=""
                ></v-select>
              </div>
            </v-flex>

            <v-flex md2>
              <label class="lab-for right black--text">Ncr no</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-text-field v-model="detail.ncr_no" placeholder="Enter the value" outline></v-text-field>
              </div>
            </v-flex>

            <v-flex md2>
              <label class="lab-for right black--text">Objective evidence</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-text-field
                  v-model="detail.objective_evidence"
                  placeholder="Enter the value"
                  outline
                ></v-text-field>
              </div>
            </v-flex>

            <v-flex md2>
              <label class="lab-for right black--text">Root cause</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-text-field v-model="detail.root_cause" placeholder="Enter the value" outline></v-text-field>
              </div>
            </v-flex>

            <v-flex md2>
              <label class="lab-for right black--text">Correction</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-text-field v-model="detail.correction" placeholder="Enter the value" outline></v-text-field>
              </div>
            </v-flex>

            <v-flex md2>
              <label class="lab-for right black--text">Correction action</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-text-field
                  v-model="detail.correction_action"
                  placeholder="Enter the value"
                  outline
                ></v-text-field>
              </div>
            </v-flex>

            <v-flex md2>
              <label class="lab-for right black--text">Nc statement</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-textarea v-model="detail.nc_statement" name="input-7-4" outline></v-textarea>
              </div>
            </v-flex>

            <v-flex md2>
              <label class="lab-for right black--text">Containment action</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-textarea outline name="input-7-4" v-model="detail.containment_action"></v-textarea>
              </div>
            </v-flex>
          </v-layout>
          <v-flex md12 offset-md2>
            <v-btn :disabled="!valid" color="success" @click="validate">Save</v-btn>
            <v-btn color="error" @click="reset">cancel</v-btn>
          </v-flex>
        </v-form>
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
      valid: true,
      auditArea: [],
    };
  },
  mounted() {
    this.getAreAudit();
  },
  methods: {
    validate() {
      if (this.$refs.form.validate()) {
        this.snackbar = true;
        axios
          .post(this.$apiUrl + "mr/non-conf/", {
            area_of_audit: this.detail.area_of_audit,
            ncr_no: this.detail.ncr_no,
            customer_order: this.customer_order,
            nc_statement: this.detail.nc_statement,
            objective_evidence: this.detail.objective_evidence,
            root_cause: this.detail.root_cause,
            containment_action: this.detail.containment_action,
            correction: this.detail.correction,
            correction_action: this.detail.correction_action,
            owner: this.$owner
          })
          .then(function(response) {
            console.log(response.data);
            router.push("/mr-non-conformance/" + response.data.id);
          })
          .catch(function(error) {
            console.log(error);
          });
      }
    },
    getAreAudit() {
      var self = this;
      axios
        .get(this.$apiUrl + "mr/internal-audit-plan/")
        .then(function(response) {
          self.auditArea = response.data;
        })
        .catch(function(error) {
          console.log(error.data);
        });
    },
    reset() {
      this.$refs.form.reset();
    }
  }
};
</script>


<style scoped>
.lab-for {
  line-height: 44px;
  margin-right: 8px;
}
</style>
