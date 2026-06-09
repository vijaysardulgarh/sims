import {
  useEffect,
  useState
} from "react";

import {
  useNavigate,
  useParams
} from "react-router-dom";

import toast from "react-hot-toast";

import AssociationMemberForm from "../components/AssociationMemberForm";

import associationMemberService from "../services/associationMemberService";

const AssociationMemberEditPage = () => {

  const { id } = useParams();

  const navigate = useNavigate();

  const [loading,
    setLoading] =
    useState(false);

  const [initialData,
    setInitialData] =
    useState({});

  useEffect(() => {

    fetchMember();

  }, [id]);

  const fetchMember = async () => {

    try {

      const response =
        await associationMemberService.getById(
          id
        );

      setInitialData(
        response.data
      );

    } catch (error) {

      console.error(error);

    }
  };

  const handleSubmit = async (
    data
  ) => {

    try {

      setLoading(true);

      await associationMemberService.update(
        id,
        data
      );

      toast.success(
        "Updated successfully"
      );

      navigate(
        "/dashboard/associations/association-members"
      );

    } catch (error) {

      console.error(error);

      toast.error(
        "Update failed"
      );

    } finally {

      setLoading(false);
    }
  };

  return (

    <div className="space-y-6">

      <h1 className="text-2xl font-bold">

        Edit Member

      </h1>

      <AssociationMemberForm

        initialData={initialData}

        onSubmit={handleSubmit}

        loading={loading}
      />

    </div>
  );
};

export default AssociationMemberEditPage;