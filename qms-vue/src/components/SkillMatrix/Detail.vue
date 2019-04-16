<template>
  <div id>
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">Skill Matrix Detail</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right">
          <div>
            <v-tooltip bottom>
              <template v-slot:activator="{ on }">
                <router-link :to="{path: '/skill-matrix-edit/'+detail.id }">
                <v-btn icon v-on="on" ref="fileInput">
                  <v-icon color="info">edit</v-icon>
                </v-btn>
                </router-link>
              </template>
              <span>Edit</span>
            </v-tooltip>
            <v-tooltip bottom>
              <template v-slot:activator="{ on }">
                <v-btn icon v-on="on" ref="fileInput">
                  <v-icon color="red">delete</v-icon>
                </v-btn>
              </template>
              <span>Delete</span>
            </v-tooltip>
          </div>
        </div>
      </v-flex>
    </v-layout>
    <!-- Details-list -->
    <v-layout container>
      <v-flex xs12 sm12 md12>
        <v-card>
          <v-layout class="lay-des heder-card" row wrap>
            <v-flex md3 sm6>
              <p>
                <strong>Department :</strong>
                {{ detail.depaertment }}
              </p>
            </v-flex>
            <v-flex md3 sm6>
              <p>
                <strong>Designation :</strong>
                {{ detail.designation }}
              </p>
            </v-flex>
            <v-flex md3 sm6>
              <p>
                <strong>Date :</strong>
                {{ detail.created_On }}
              </p>
            </v-flex>
          </v-layout>
          <div class="under-line"></div>
          <!-- Dtails -->
          <v-layout class="lay-des" row wrap>
            <v-flex md6>
              <p>
                <strong>Employee ID :</strong>
                {{ detail.empName }}
              </p>
              <p>
                <strong>Name :</strong>
                {{ detail.empName }}
              </p>
              <p>
                <strong>Department :</strong>
                {{ detail.depaertment }}
              </p>
              <p>
                <strong>Designation :</strong>
                {{ detail.designation }}
              </p>
              <p>
                <strong>Scroing Crieteria :</strong>
                <span v-if="detail.scoring_crieteria == '1'">Need Training</span>
                <span v-else-if="detail.scoring_crieteria == '2'">Can Work under supervision</span>
                <span v-else-if="detail.scoring_crieteria == '3'">Can Work alone</span>
                <span v-else>Can work & Train other</span>
              </p>
            </v-flex>
          </v-layout>
          <div class="under-line"></div>
          <v-layout class="lay-des" row wrap>
            <v-flex xs12>
              <p>
                <strong>SKILLS</strong>
              </p>
            </v-flex>
            <!--first list-->
            <v-flex md6>
              <v-layout row>
                <v-flex md7>
                  <p>Drawing studing skills</p>
                  <p>Usage of general gauges</p>
                  <p>Usage of general instruments</p>
                  <p>Usage of product specific gauges</p>
                  <p>Quality documentation</p>
                  <p>CMM operating</p>
                  <p>PP Operating</p>
                </v-flex>
                <v-flex md2>
                  <p>{{ detail.drawing_studying_skills }}</p>
                  <p>{{ detail.usage_of_general_gauges }}</p>
                  <p>{{ detail.usage_of_general_instruments }}</p>
                  <p>{{ detail.usage_of_product_specific_gauges }}</p>
                  <p>{{ detail.quality_documentation }}</p>
                  <p>{{ detail.cmm_operating }}</p>
                  <p>{{ detail.pp_operating }}</p>
                </v-flex>
              </v-layout>
            </v-flex>
            <!--second list-->
            <v-flex md6>
              <v-layout row>
                <v-flex md7>
                  <p>Basic machining knowledge</p>
                  <p>Internal verification skills</p>
                  <p>Inspection skill</p>
                  <p>Visual inspection skill</p>
                  <p>2D height gauge operating</p>
                  <p>Operating surface roughness tester</p>
                  <p>Microscope Handeling</p>
                </v-flex>
                <v-flex md2>
                  <p>{{ detail.basic_machining_knowledge }}</p>
                  <p>{{ detail.internal_verification_skills }}</p>
                  <p>{{ detail.inspection_skill }}</p>
                  <p>{{ detail.visual_inspection_skill }}</p>
                  <p>{{ detail.d_height_gauge_operating }}</p>
                  <p>{{ detail.operating_surface_roughness_tester }}</p>
                  <p>{{ detail.microscope_handeling }}</p>
                </v-flex>
              </v-layout>
            </v-flex>
            <!--total value -->
            <v-flex xs11>
              <div class="total-value">
                <p>
                  <strong>TOTAL :</strong>
                  <span>
                    {{
                    parseInt(detail.drawing_studying_skills) +
                    parseInt(detail.usage_of_general_gauges) +
                    parseInt(detail.usage_of_general_instruments) +
                    parseInt(detail.usage_of_product_specific_gauges) +
                    parseInt(detail.quality_documentation) +
                    parseInt(detail.cmm_operating) +
                    parseInt(detail.pp_operating) +
                    parseInt(detail.basic_machining_knowledge) +
                    parseInt(detail.internal_verification_skills) +
                    parseInt(detail.inspection_skill) +
                    parseInt(detail.visual_inspection_skill) +
                    parseInt(detail.d_height_gauge_operating) +
                    parseInt(detail.operating_surface_roughness_tester) +
                    parseInt(detail.microscope_handeling)
                    }}
                  </span>
                </p>
              </div>
            </v-flex>
            <!-- end total value -->
            <!--total value -->
            <div class="under-line"></div>
            <v-flex xs12 sm12 md12>
              <div class="mrt20">
                <span class="ap-sp">
                  <strong>Prepred By :</strong>
                  <span>{{detail.prepredBy}}</span>
                </span>
                <span class="right">
                  <strong>Approved By :</strong>
                  <span>{{detail.approvedBy}}</span>
                </span>
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
      detail: []
    };
  },
  mounted() {
    this.getdetails();
  },
  methods: {
    getdetails() {
      var ts = window.location.pathname.split("/");
      var parQuery = ts[ts.length - 1];
      var self = this;
      axios
        .get(this.$apiUrl + "skill-matrix/" + parQuery)
        .then(function(response) {
          self.detail = response.data;
        })
        .catch(function(error) {
          console.log(error.data);
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
.heder-card p {
  margin: 0px;
}

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
.mrt20 {
  margin-top: 20px;
}
</style> 







