import api from "../../../../services/api/axios";

const associationRoleAssignmentService = {

  // =========================
  // GET ALL ASSIGNMENTS
  // =========================

  getAssignments: async () => {

    const response =
      await api.get(
        "/associations/association-role-assignments/"
      );

    return response.data;
  },

  // =========================
  // GET SINGLE ASSIGNMENT
  // =========================

  getAssignment: async (id) => {

    const response =
      await api.get(
        `/associations/association-role-assignments/${id}/`
      );

    return response.data;
  },

  // =========================
  // CREATE ASSIGNMENT
  // =========================

  createAssignment: async (data) => {

    const response =
      await api.post(
        "/associations/association-role-assignments/",
        data
      );

    return response.data;
  },

  // =========================
  // UPDATE ASSIGNMENT
  // =========================

  updateAssignment: async (
    id,
    data
  ) => {

    const response =
      await api.put(
        `/associations/association-role-assignments/${id}/`,
        data
      );

    return response.data;
  },

  // =========================
  // DELETE ASSIGNMENT
  // =========================

  deleteAssignment: async (id) => {

    const response =
      await api.delete(
        `/associations/association-role-assignments/${id}/`
      );

    return response.data;
  },
};

export default associationRoleAssignmentService;