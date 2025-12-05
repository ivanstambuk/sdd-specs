# Profile Specification — EC-OPRF + FHE (c3/ec-oprf-fhe)

## Overview

This document defines profiles for the `ec-oprf-fhe-c3` unit. Profiles describe
combinations of features and HTTP APIs that an implementation MAY support. All
profiles share the same cryptographic algorithms and data-model described in
`spec.md`.

- Namespace: `c3/ec-oprf-fhe`
- Unit identifier: `ec-oprf-fhe-c3`
- Version: `1.0.0`
- Status: `draft`

## Profiles

### Profile `oprf-only`

**Goal:** Support EC-OPRF-based password breach checks with k-anonymous encrypted
buckets, without exposing the BFV FHE evaluate route.

**Required features:**

- `ec-oprf-core`
- `buckets-k-anon`

**External HTTP APIs:**

- `GET /v1/metadata`
- `POST /v1/oprf/evaluate`
- `GET /v1/buckets`
- `HEAD /v1/buckets`

**Non-goals:**

- No requirement to implement `/v1/fhe/evaluate`.
- No requirement to expose homomorphic evaluation parameters or contexts beyond
  what is needed for EC-OPRF and bucket handling.

### Profile `oprf-plus-fhe`

**Goal:** Support both EC-OPRF + k-anonymous buckets and a BFV FHE membership
check route for password digests.

**Required features:**

- `ec-oprf-core`
- `buckets-k-anon`
- `fhe-bfv-membership`

**External HTTP APIs:**

- `GET /v1/metadata`
- `POST /v1/oprf/evaluate`
- `GET /v1/buckets`
- `HEAD /v1/buckets`
- `POST /v1/fhe/evaluate`

**Non-goals:**

- No guarantee of ciphertext wire-format interoperability between different
  BFV/FHE libraries.
- No obligation to expose Paillier-OPE or any other protocol family.

## Goals and Non-goals

### Goals (all profiles)

- Provide a stable, implementation-agnostic description of EC-OPRF + buckets and
  BFV FHE membership checks.
- Allow independent client and server implementations to interoperate via HTTP
  and JSON without sharing internal code.
- Make it possible to generate conformance tests and fixtures that exercise the
  OPRF, bucket, and FHE flows end-to-end.

### Non-goals (all profiles)

- Defining a normative BFV ciphertext serialization format that guarantees
  cross-library decryption compatibility.
- Mandating any particular programming language, runtime, or cryptographic
  library.
- Specifying operational concerns such as deployment, key storage, or TLS
  termination.
