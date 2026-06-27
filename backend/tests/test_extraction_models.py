"""Unit tests for app/models/extraction.py — no network, no DB."""
import pytest
from pydantic import ValidationError

from app.models.extraction import BillingRecord, ExtractionOutput, FlaggedRecord


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _minimal_billing(**overrides) -> dict:
    base = {
        "treatment_date": "01/15/2023",
        "provider": "Acme Medical Center",
        "page": "1",
    }
    base.update(overrides)
    return base


def _minimal_flagged(**overrides) -> dict:
    base = {
        "reason": "Missing CPT code",
        "page": "2",
        "severity": "medium",
    }
    base.update(overrides)
    return base


# ---------------------------------------------------------------------------
# BillingRecord
# ---------------------------------------------------------------------------

class TestBillingRecord:
    def test_minimal_valid_record(self):
        r = BillingRecord(**_minimal_billing())
        assert r.treatment_date == "01/15/2023"
        assert r.provider == "Acme Medical Center"
        assert r.page == "1"

    def test_cpt_codes_defaults_empty(self):
        r = BillingRecord(**_minimal_billing())
        assert r.cpt_codes == []

    def test_cpt_codes_accepts_list(self):
        r = BillingRecord(**_minimal_billing(cpt_codes=["99213", "71046"]))
        assert r.cpt_codes == ["99213", "71046"]

    def test_cpt_codes_accepts_empty_list(self):
        r = BillingRecord(**_minimal_billing(cpt_codes=[]))
        assert r.cpt_codes == []

    def test_nullable_fields_accept_none(self):
        r = BillingRecord(
            **_minimal_billing(
                description=None,
                total_charges=None,
                ins_paid=None,
                adjustment=None,
                payments=None,
                balance=None,
            )
        )
        assert r.description is None
        assert r.total_charges is None
        assert r.ins_paid is None
        assert r.adjustment is None
        assert r.payments is None
        assert r.balance is None

    def test_nullable_fields_absent_default_none(self):
        r = BillingRecord(**_minimal_billing())
        assert r.description is None
        assert r.total_charges is None
        assert r.ins_paid is None
        assert r.adjustment is None
        assert r.payments is None
        assert r.balance is None

    def test_float_fields_accept_values(self):
        r = BillingRecord(
            **_minimal_billing(
                total_charges=1500.00,
                ins_paid=1200.00,
                adjustment=200.00,
                payments=50.00,
                balance=50.00,
            )
        )
        assert r.total_charges == 1500.00
        assert r.balance == 50.00

    def test_page_accepts_single_string(self):
        r = BillingRecord(**_minimal_billing(page="6"))
        assert r.page == "6"

    def test_page_accepts_range_string(self):
        r = BillingRecord(**_minimal_billing(page="6-7"))
        assert r.page == "6-7"

    def test_insurers_defaults_empty(self):
        r = BillingRecord(**_minimal_billing())
        assert r.insurers == []

    def test_third_parties_defaults_empty(self):
        r = BillingRecord(**_minimal_billing())
        assert r.third_parties == []

    def test_treatment_date_range_string(self):
        r = BillingRecord(**_minimal_billing(treatment_date="01/01/2022 - 12/31/2022"))
        assert r.treatment_date == "01/01/2022 - 12/31/2022"

    def test_missing_required_treatment_date_raises(self):
        with pytest.raises(ValidationError):
            BillingRecord(provider="Clinic", page="1")

    def test_missing_required_provider_raises(self):
        with pytest.raises(ValidationError):
            BillingRecord(treatment_date="01/01/2023", page="1")

    def test_missing_required_page_raises(self):
        with pytest.raises(ValidationError):
            BillingRecord(treatment_date="01/01/2023", provider="Clinic")


# ---------------------------------------------------------------------------
# FlaggedRecord
# ---------------------------------------------------------------------------

class TestFlaggedRecord:
    def test_severity_low(self):
        r = FlaggedRecord(**_minimal_flagged(severity="low"))
        assert r.severity == "low"

    def test_severity_medium(self):
        r = FlaggedRecord(**_minimal_flagged(severity="medium"))
        assert r.severity == "medium"

    def test_severity_high(self):
        r = FlaggedRecord(**_minimal_flagged(severity="high"))
        assert r.severity == "high"

    def test_invalid_severity_raises(self):
        with pytest.raises(ValidationError):
            FlaggedRecord(**_minimal_flagged(severity="critical"))

    def test_row_defaults_none(self):
        r = FlaggedRecord(**_minimal_flagged())
        assert r.row is None

    def test_row_accepts_zero(self):
        r = FlaggedRecord(**_minimal_flagged(row=0))
        assert r.row == 0

    def test_row_accepts_positive_int(self):
        r = FlaggedRecord(**_minimal_flagged(row=5))
        assert r.row == 5

    def test_row_rejects_negative(self):
        with pytest.raises(ValidationError):
            FlaggedRecord(**_minimal_flagged(row=-1))

    def test_fields_defaults_empty(self):
        r = FlaggedRecord(**_minimal_flagged())
        assert r.fields == []

    def test_fields_accepts_list(self):
        r = FlaggedRecord(**_minimal_flagged(fields=["total_charges", "ins_paid"]))
        assert r.fields == ["total_charges", "ins_paid"]

    def test_missing_reason_raises(self):
        with pytest.raises(ValidationError):
            FlaggedRecord(page="1", severity="low")

    def test_missing_page_raises(self):
        with pytest.raises(ValidationError):
            FlaggedRecord(reason="Something wrong", severity="low")

    def test_missing_severity_raises(self):
        with pytest.raises(ValidationError):
            FlaggedRecord(reason="Something wrong", page="1")


# ---------------------------------------------------------------------------
# ExtractionOutput
# ---------------------------------------------------------------------------

class TestExtractionOutput:
    def test_empty_defaults(self):
        out = ExtractionOutput()
        assert out.records == []
        assert out.flagged == []

    def test_explicit_empty_lists(self):
        out = ExtractionOutput(records=[], flagged=[])
        assert out.records == []
        assert out.flagged == []

    def test_with_records_and_flagged(self):
        rec = BillingRecord(**_minimal_billing(total_charges=500.0))
        flag = FlaggedRecord(**_minimal_flagged(row=0, severity="high"))
        out = ExtractionOutput(records=[rec], flagged=[flag])
        assert len(out.records) == 1
        assert len(out.flagged) == 1
        assert out.records[0].total_charges == 500.0
        assert out.flagged[0].severity == "high"

    def test_multiple_records(self):
        recs = [
            BillingRecord(**_minimal_billing(treatment_date=f"01/0{i}/2023"))
            for i in range(1, 4)
        ]
        out = ExtractionOutput(records=recs)
        assert len(out.records) == 3

    def test_records_preserve_order(self):
        dates = ["03/01/2023", "01/01/2023", "02/01/2023"]
        recs = [BillingRecord(**_minimal_billing(treatment_date=d)) for d in dates]
        out = ExtractionOutput(records=recs)
        assert [r.treatment_date for r in out.records] == dates
