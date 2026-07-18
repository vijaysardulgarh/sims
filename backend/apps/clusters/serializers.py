# =============================================================================
# clusters/serializers.py
# =============================================================================

from rest_framework import serializers

from apps.clusters.models import Cluster


class ClusterSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Cluster

        fields = [

            "id",

            # ======================================
            # BASIC INFORMATION
            # ======================================

            "name",
            "code",
            "slug",
            "description",

            # ======================================
            # CRC INFORMATION
            # ======================================

            "crc_name",
            "crc_designation",
            "crc_phone",
            "crc_email",

            # ======================================
            # OFFICE CONTACT INFORMATION
            # ======================================

            "email",
            "phone",
            "address",

            # ======================================
            # STATUS
            # ======================================

            "is_active",

            # ======================================
            # AUDIT
            # ======================================

            "created_at",
            "updated_at",

        ]

        read_only_fields = [

            "slug",
            "created_at",
            "updated_at",

        ]