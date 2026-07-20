import {
    useEffect,
    useState,
} from "react";

import {
    useNavigate,
    useParams,
} from "react-router-dom";

import toast from "react-hot-toast";

import SchoolForm from "../components/SchoolForm";

import schoolService from "../services/schoolService";

import {
    getClusters,
} from "../../../clusters/services/clusterService";

const EditSchoolPage = () => {

    const { id } = useParams();

    const navigate = useNavigate();

    const [school, setSchool] = useState(null);

    const [clusters, setClusters] = useState([]);

    const [loading, setLoading] = useState(false);

    useEffect(() => {

        loadData();

    }, [id]);

    const loadData = async () => {

        try {

            setLoading(true);

            const [schoolData, clusterData] = await Promise.all([

                schoolService.getSchool(id),

                getClusters(),

            ]);

            console.log("School:", schoolData);
            console.log("Clusters:", clusterData);

            // If getSchool() returns response.data
            setSchool(schoolData);

            // Handle paginated and non-paginated cluster APIs
            const clusterList = Array.isArray(clusterData)
                ? clusterData
                : clusterData.results || [];

            setClusters(clusterList);

        } catch (error) {

            console.error(error);

            toast.error("Failed to load school");

        } finally {

            setLoading(false);

        }

    };

    const handleSubmit = async (formData) => {

        try {

            setLoading(true);

            await schoolService.updateSchool(id, formData);

            toast.success("School updated successfully");

            navigate("/dashboard/schools/schools");

        } catch (error) {

            console.error(error);

            toast.error("Failed to update school");

        } finally {

            setLoading(false);

        }

    };

    if (!school) {

        return (
            <div className="p-6">
                Loading...
            </div>
        );

    }

    return (

        <SchoolForm
            initialData={school}
            clusters={clusters}
            loading={loading}
            onSubmit={handleSubmit}
        />

    );

};

export default EditSchoolPage;